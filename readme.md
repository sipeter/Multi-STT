## Multi-STT: 多引擎语音转文本工具



**Multi-STT**  是一个使用 FastAPI 构建的语音转文本 API，它整合了三个强大的语音识别引擎：

* **Whisper:**  由 OpenAI 开发的强大语音识别模型。
* **Faster Whisper:**  Whisper 模型的更快实现，使用 CTranslate2 进行推理加速。
* **FunASR:**  阿里巴巴达摩院开发的一个开源自动语音识别(ASR)系统。

通过结合多个引擎，Multi-STT 可以提供更准确、更强大的语音转文本功能。

### 功能

* 接收音频文件（例如 WAV 格式）并将其转录为文本。
* 支持多种语言，包括英语、中文等（具体取决于所使用的模型）。
* 可以选择使用不同的语音识别引擎（Whisper, Faster Whisper, FunASR）。
* 提供易于使用的 API 接口，方便集成到其他应用程序中。

### 安装

1. 克隆项目仓库：

   ```bash
   git clone https://github.com/sipeter/Multi-STT.git
   cd Multi-STT
   ```

2. 创建虚拟环境并激活：

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. 安装依赖项：

   ```bash
   pip install -r requirements.txt
   ```

### 使用方法

1. 启动 API 服务器：

   ```bash
   python fasterwhisper_api.py 
   ```
   或
   ```bash
   python funasr_api.py 
   ```
   (根据需要选择要使用的引擎)

2. 发送音频文件到 API 接口进行转录：

   ```bash
   curl -X POST -F "file=@audio.wav" http://localhost:8002/v1/audio/transcriptions
   ```

   (将  `audio.wav`  替换为你的音频文件路径， `8002` 替换为 API 服务器的端口号)

### 配置

*  你可以在  `fasterwhisper_api.py`  和  `funasr_api.py`  文件中修改 API 服务器的端口号和其他配置选项。
*  你可以在  `requirements.txt`  文件中指定要使用的  `whisper`  、  `faster-whisper`  和  `funasr`  的版本。

### 贡献

欢迎提交 issue 和 PR 来改进 Multi-STT 项目。

### 许可证

MIT License


## Multi-STT: Multi-Engine Speech-to-Text API

**Multi-STT** is a FastAPI-based speech-to-text API that leverages the power of three leading speech recognition engines:

* **Whisper:** A robust and accurate speech recognition model developed by OpenAI.
* **Faster Whisper:** A faster implementation of the Whisper model, using CTranslate2 for inference acceleration.
* **FunASR:** An open-source Automatic Speech Recognition (ASR) toolkit developed by Alibaba DAMO Academy.

By combining multiple engines, Multi-STT offers enhanced accuracy and robustness for your speech-to-text needs.

### Features

* Transcribes audio files (e.g., WAV format) into text.
* Supports various languages, including English, Chinese, and more (depending on the models used).
* Offers the flexibility to choose between different speech recognition engines (Whisper, Faster Whisper, FunASR).
* Provides a user-friendly API interface for easy integration into other applications.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/sipeter/Multi-STT.git
   cd Multi-STT
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Start the API server:

   ```bash
   python fasterwhisper_api.py 
   ```
   or
   ```bash
   python funasr_api.py 
   ```
   (Choose the engine you want to use)

2. Send an audio file to the API endpoint for transcription:

   ```bash
   curl -X POST -F "file=@audio.wav" http://localhost:8002/v1/audio/transcriptions
   ```

   (Replace `audio.wav` with your audio file path and `8002` with the API server port)

### Configuration

*  You can modify the API server port and other configuration options in the `fasterwhisper_api.py` and  `funasr_api.py` files.
*  You can specify the versions of `whisper`, `faster-whisper`, and `funasr` you want to use in the `requirements.txt` file.

### Contributing

Contributions are welcome! Feel free to submit issues and pull requests to improve Multi-STT.

### License

MIT License 

