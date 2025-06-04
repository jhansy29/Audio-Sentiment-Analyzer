# 🎙️ Vertex AI Audio Transcriber & Sentiment Analyzer

This project is a voice-enabled web application that allows users to **record speech**, automatically **transcribe it to text**, and perform **sentiment analysis** using **Google Vertex AI Generative Model**.

📍 Developed as part of Conversational AI Project 3  
🌐 Deployed on Google Cloud Run for public access


---

## 🚀 Features

- 🎤 **Record Audio** directly from the browser using MediaRecorder API
- ✍️ **Speech-to-Text Transcription** powered by Vertex AI
- 😊 **Sentiment Analysis** (Positive, Neutral, or Negative)
- 📥 Downloadable `.txt` transcript with embedded sentiment result
- ☁️ Hosted using **Docker + Google Cloud Run**

---

## 🛠️ Tech Stack

| Component     | Tech Used                        |
|---------------|----------------------------------|
| Frontend      | HTML + JavaScript (MediaRecorder API) |
| Backend       | Python (Flask)                   |
| AI Services   | Google Vertex AI (Gemini Model)  |
| Deployment    | Google Cloud Run (Dockerized)    |

---

## 📦 Installation

```bash
git clone https://github.com/jhansy29/conv_ai_project3.git
cd conv_ai_project3
pip install -r requirements.txt
python main.py
