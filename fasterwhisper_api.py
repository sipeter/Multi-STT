# fasterwhisper_api.py
import os
from fastapi import FastAPI, UploadFile, File
from typing import Dict
import tempfile
from fasterwhisper_asr import execute_asr
import torch # 导入torch库

app = FastAPI()

# 预加载模型，避免每次请求都加载
model = None
model_size = "medium"  # 可以根据需要修改默认模型大小
language = "zh"  # 可以根据需要修改默认语言
precision = "float16"  # 可以根据需要修改默认精度

@app.on_event("startup")
async def load_model():
    global model
    from faster_whisper import WhisperModel
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    model = WhisperModel(model_size, device=device, compute_type=precision)

@app.post("/v1/audio/transcriptions")
async def transcribe_audio(file: UploadFile = File(...), language: str = None):
    """
    接收音频文件并返回转录文本.

    Args:
        file (UploadFile): 音频文件
        language (str, optional): 音频语言. 默认自动识别.

    Returns:
        Dict: 包含转录文本的字典.
    """
    # 创建临时文件
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_file:
        # 写入上传的文件内容
        content = await file.read()
        temp_file.write(content)
        temp_file.flush()

        # 使用临时文件路径调用 FasterWhisper 进行转录
        segments, info = model.transcribe(
            audio          = temp_file.name,
            beam_size      = 5,
            vad_filter     = True,
            vad_parameters = dict(min_silence_duration_ms=700),
            language       = "zh"  # 明确指定语言为中文
         )
        text = ''
        for segment in segments:
            text += segment.text

    # 删除临时文件
    os.unlink(temp_file.name)

    # 返回转录结果
    return {"text": text}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("fasterwhisper_api:app", host="0.0.0.0", port=8002)