CHCP 65001
@echo off


:: 激活虚拟环境
call venv\Scripts\activate.bat

:: 运行 Whisper 项目
python fasterwhisper_api.py  