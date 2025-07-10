
# 🎙️ AI Text-to-Speech Web App with Flask & ElevenLabs

This is a full-featured Text-to-Speech (TTS) web application built using **Flask** and **ElevenLabs API**, allowing users to convert input text or uploaded text files into realistic voice audio.

## ✨ Features

* 🔐 **Login Authentication**
  Secure login using session-based authentication.

* 🗣️ **Multi-Voice Support**
  Choose from multiple realistic voices provided by ElevenLabs.

* 📄 **Text File Upload**
  Upload `.txt` files for speech generation.

* 🎧 **Audio Preview & Download**
  Generated audio plays in the browser and is also available for download.

* 🕘 **Audio History**
  View previously generated audio files in the history section.

* 🗑️ **Clear History**
  Option to delete all generated audio files with a single click.

* 🎨 **Modern UI with Moving Background**
  Clean, responsive, and animated UI for a better experience.

---

## 🖼️ Screenshots

* ✅ Login Page
* ✅ Home with TTS generation
* ✅ View History & Clear History
 
---

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/tts-flask-elevenlabs.git
cd tts-flask-elevenlabs
```

### 2. Install Dependencies

Ensure you have Python 3.8+ installed.

```bash
pip install -r requirements.txt
```

### 3. Set Up ElevenLabs API

Create a `.env` file in the root folder:

```env
ELEVENLABS_API_KEY=your_api_key_here
```

You can get your API key from [https://www.elevenlabs.io](https://www.elevenlabs.io).

### 4. Run the App

```bash
python app.py
```

Visit: `http://127.0.0.1:5000`

---

## 🔐 Default Login

* **Username**: `Manika`
* **Password**: `Manika@2004`
  *(You can update this in `app.py` for security.)*

---

## 🗃️ Folder Structure

```
tts_app_final/
├── app.py
├── .env
├── static/
│   ├── styles.css
│   └── *.mp3
├── templates/
│   ├── index.html
│   ├── login.html
│   └── history.html
├── requirements.txt
└── README.md
```
