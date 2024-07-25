# funasr_api.py
import os
from fastapi import FastAPI, UploadFile, File
from typing import Dict
import tempfile
from funasr_asr import only_asr
import torchaudio  # 导入 torchaudio
import modelscope  # 导入 modelscope

app = FastAPI()



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

        # 使用临时文件路径调用 FunASR 进行转录
        text = only_asr(temp_file.name)

    # 删除临时文件
    os.unlink(temp_file.name)

    # 返回转录结果
    return {"text": text}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("funasr_api:app", host="0.0.0.0", port=8001)