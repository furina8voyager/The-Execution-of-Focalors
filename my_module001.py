import os
# 设置镜像加速（可选，下载慢时加上）
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'

from huggingface_hub import snapshot_download

# 下载模型到 D:\models 目录
snapshot_download(
    repo_id="sipeed/sipeed/Qwen3-VL-2B-Instruct-GPTQ-Int4-AX630C-P320-CTX448-maixcam2",
    local_dir="D:/models",
    local_dir_use_symlinks=False
)

