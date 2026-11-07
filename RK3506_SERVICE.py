from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import time
import sys

try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

class RequestHandler(BaseHTTPRequestHandler):
    def _send_json(self, code, obj):
        body = json.dumps(obj, ensure_ascii=False).encode('utf-8')
        self.send_response(code)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self):

        path = self.path.split('?')[0]
        if path != '/process':
            self._send_json(404, {"ok": False, "error": "unknown path"})
            return

        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)

        try:
            data = json.loads(post_data.decode('utf-8'))
            print("\nRK3506 收到数据")
            print(json.dumps(data, ensure_ascii=False, indent=2))
        except Exception as e:
            print("JSON 解析失败:", e)
            self._send_json(400, {"ok": False, "error": "invalid json"})
            return

        #二次处理
        results = data.get("results", [])
        first_result = results[0] if results else {}
        label = first_result.get("label", "unknown")
        confidence = first_result.get("confidence", 0.0)

        if label == "disease" and confidence >= 0.8:
            final_status = "danger"
            risk_level = 3
            advice = "建议立即人工复核并启动通风"
        elif label == "disease":
            final_status = "warning"
            risk_level = 2
            advice = "建议持续观察"
        else:
            final_status = "normal"
            risk_level = 1
            advice = "状态正常"

        # 返回给主机处理结果
        result = {
            "device_id": data.get("device_id"),
            "final_status": final_status,
            "risk_level": risk_level,
            "advice": advice,
            "processed_at": time.strftime("%Y-%m-%d %H:%M:%S")
        }

        self._send_json(200, result)

    def log_message(self, fmt, *args):
        print("[RK3506]", self.address_string(), fmt % args)


if __name__ == '__main__':
    print("RK3506 处理服务启动,监听: 0.0.0.0:8081")

    server = HTTPServer(('0.0.0.0', 8081), RequestHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n已停止")
        server.server_close()