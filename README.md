# Kim - The Virtual Voice Assistant 🗣️🤖

**Kim** is a Python-based virtual voice assistant that can understand voice commands and perform tasks like opening websites, playing music, reading live news, and even responding intelligently using NVIDIA's AI model via the OpenAI SDK.

This project demonstrates the integration of speech recognition, text-to-speech, API usage, and AI response generation — all in one Python application.

## ✨ Features

- 🎤 **Voice Activation** with wake-word detection
- 🌐 **Opens websites** like Google, YouTube, Facebook, etc.
- 🎵 **Plays music** from a predefined song library
- 📰 **Reads real-time news** using the NewsAPI
- 🧠 **AI-powered responses** using NVIDIA LLM (via OpenAI SDK)
- 🔊 **Speaks replies** using both gTTS (Google TTS) and pyttsx3
- 📦 Easy to install with `requirements.txt`

## 🛠️ Tech Stack

- `Python 3`
- `SpeechRecognition` – for voice input
- `gTTS` & `pyttsx3` – for text-to-speech
- `pygame` – to play audio files
- `requests` – for API calls (NewsAPI)
- `openai` – for AI response (NVIDIA LLM)
- `pyaudio` – backend for microphone input
- 
## 🚀 How to Run the Project

1. **Clone this repo** or [Download ZIP](https://github.com/21Aditya-PY/Kim-the-virtual-assistant/archive/refs/heads/main.zip)

2. **Install all dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   > ⚠️ If `pyaudio` fails, run these instead:
   ```bash
   pip install pipwin
   pipwin install pyaudio
   ```

3. **Run the voice assistant**:
   ```bash
   python main.py
   ```
   
## 🎙️ How It Works

- Say **"Kim"** or **"Hello"** to activate the assistant
- Give a command like:
  - "Open Google"
  - "Play shapeofyou"
  - "What's the news?"
  - Ask any general question like "What is Python?"
- The assistant will respond via voice

## 🔐 API Keys Used

- **NewsAPI** – for fetching latest headlines
- **NVIDIA LLM** – for AI-generated responses (via OpenAI SDK)

> ⚠️ Remember to keep your API keys private in production environments.

---

## 👨‍💻 Author

**Aditya Pathak**  
📍 India  
🌐 [GitHub](https://github.com/21Aditya-PY) | [LinkedIn](https://www.linkedin.com/in/aditya-pathak-b0700228b/)

---

## 📌 Disclaimer

This project is part of my learning journey in AI, Python automation, and voice-based interaction. Feedback and contributions are always welcome!
