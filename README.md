# OllamaUI

A web interface for [Ollama](https://ollama.ai/).

<video src="https://github.com/Pleym/OllamaUI/raw/main/demo/video.mp4" controls="controls" style="max-width: 100%;">
</video>

## Features

- **Streaming**: Real-time typewriter effect for AI responses.
- **Markdown Support**: Code blocks and formatting rendered beautifully.
- **Model Selection**: Automatically detects installed Ollama models.

## Prerequisites
1.  **Ollama**: Must be installed and running.
    - [Download Ollama](https://ollama.ai/download)
    - Run: `ollama serve`
2.  **Python 3**: Required to run the proxy server.

## Installation

1.  Clone or download this repository.
2.  Install the required Python packages:
    ```bash
    pip install flask requests
    ```

## Usage

1.  Start the proxy server:
    ```bash
    python3 proxy.py
    ```
2.  Open your browser and navigate to:
    [http://localhost:3000](http://localhost:3000)

## Credits
Created by [Pleym](https://abldorian.dev).
