from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import requests
import time
import threading
import json
import datetime

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///grain_monitor.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class DetectionRecord(db.Model):
    __tablename__ = 'detection_records'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    device_id = db.Column(db.String(50), nullable=False)
    frame_id = db.Column(db.Integer)
    maixcam_timestamp = db.Column(db.String(50))
    results_json = db.Column(db.Text)  # 原始检测数据
    final_status = db.Column(db.String(20))  # normal/warning/danger
    risk_level = db.Column(db.Integer)
    advice = db.Column(db.String(200))
    time = db.Column(db.DateTime, default=datetime.datetime.now)

    def to_dict(self):
        return {
            "id": self.id,
            "device_id": self.device_id,
            "frame_id": self.frame_id,
            "maixcam_timestamp": self.maixcam_timestamp,
            "results": json.loads(self.results_json) if self.results_json else [],
            "final_status": self.final_status,
            "risk_level": self.risk_level,
            "advice": self.advice,
            "time": self.time.strftime("%Y-%m-%d %H:%M:%S")
        }


HOST_IP = "192.168.10.101"
RK3506_URL = "http://192.168.10.10:8081/process"

lock = threading.Lock()
latest = {"updated_at": None, "maixcam_raw": None,
          "rk3506_result": None, "forward_ok": False, "error": None}


def validate(data):
    if not isinstance(data, dict):
        return False, "not a json object"
    if not data.get("device_id"):
        return False, "missing device_id"
    if data.get("msg_type") != "detection":
        return False, "msg_type must be detection"
    results = data.get("results")
    if not isinstance(results, list) or len(results) == 0:
        return False, "results empty"
    for i, r in enumerate(results):
        if not isinstance(r, dict):
            return False, f"results[{i}] not object"
        conf = r.get("confidence")
        if conf is None or isinstance(conf, bool) or not isinstance(conf, (int, float)):
            return False, f"results[{i}] bad confidence"
        if not 0 <= conf <= 1:
            return False, f"results[{i}] confidence out of range"
        bbox = r.get("bbox")
        if not isinstance(bbox, (list, tuple)) or len(bbox) != 4:
            return False, f"results[{i}] bad bbox"
        if bbox[2] <= bbox[0] or bbox[3] <= bbox[1]:
            return False, f"results[{i}] bbox coords invalid"
    if not data.get("timestamp"):
        return False, "missing timestamp"
    return True, "ok"


@app.route("/grain_state", methods=["POST"])
def grain_state():
    raw = request.get_json(silent=True) or {}
    ok, msg = validate(raw)
    if not ok:
        with lock:
            latest.update(updated_at=time.strftime("%Y-%m-%d %H:%M:%S"),
                          maixcam_raw=raw, rk3506_result=None,
                          forward_ok=False, error=msg)
        return jsonify({"ok": False, "error": msg}), 400

    # 转发到RK3506
    fwd_ok, rk_resp, err = False, None, None
    try:
        r = requests.post(RK3506_URL, json=raw, timeout=3)
        rk_resp = r.json() if r.headers.get('content-type', '').startswith('application/json') else {"text": r.text}
        fwd_ok = True
    except Exception as e:
        err = str(e)

    with lock:
        latest.update(updated_at=time.strftime("%Y-%m-%d %H:%M:%S"),
                      maixcam_raw=raw, rk3506_result=rk_resp,
                      forward_ok=fwd_ok, error=err)

    # 入库
    if fwd_ok and rk_resp:
        try:
            rec = DetectionRecord(
                device_id=raw["device_id"],
                frame_id=raw.get("frame_id"),
                maixcam_timestamp=raw.get("timestamp"),
                results_json=json.dumps(raw["results"], ensure_ascii=False),
                final_status=rk_resp.get("final_status"),
                risk_level=rk_resp.get("risk_level"),
                advice=rk_resp.get("advice"))
            db.session.add(rec)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("db error:", e)

    return jsonify({"ok": True, "forward_ok": fwd_ok, "error": err})


@app.route("/api/result")
def api_result():
    with lock:
        return jsonify(dict(latest))


@app.route("/api/history")
def api_history():
    limit = min(request.args.get("limit", 50, type=int), 500)
    recs = DetectionRecord.query.order_by(DetectionRecord.id.desc()).limit(limit).all()
    recs.reverse()
    return jsonify([r.to_dict() for r in recs])


@app.route("/api/stats")
def api_stats():
    q = lambda s: DetectionRecord.query.filter_by(final_status=s).count()
    return jsonify({"total": DetectionRecord.query.count(),
                    "normal": q("normal"), "warning": q("warning"), "danger": q("danger")})


@app.route("/")
def index():
    return "grain monitor gateway"


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    print(f"gateway on :8080, forward -> {RK3506_URL}")
    app.run(host="0.0.0.0", port=8080, threaded=True)