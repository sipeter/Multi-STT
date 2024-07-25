
# whisper_asr.py

import whisper
from fastapi import FastAPI, UploadFile, File
from typing import Dict
import tempfile
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 初始化 Whisper 模型 (选择合适的模型大小)
model = whisper.load_model("base")

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
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(file.filename)[1]) as temp_file:
        # 写入上传的文件内容
        content = await file.read()
        temp_file.write(content)
        temp_file.flush()

        # 使用临时文件路径调用 Whisper 模型进行转录
        result = model.transcribe(temp_file.name, language=language)

    # 删除临时文件
    os.unlink(temp_file.name)

    # 返回转录结果
    return {"text": result["text"]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("whisper_asr:app", host="0.0.0.0", port=8000, reload=True)



