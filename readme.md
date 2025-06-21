# 🤖 AI Chatbot (Solid.js + FastAPI + OpenRouter + Twitter Clone API)

An elegant and functional AI chatbot web application using **Solid.js (Vite)** for frontend, **FastAPI** for backend, **OpenRouter** for AI responses, and a **Twitter Clone API** to post tweets directly from the bot.

---

## 📸 Demo Preview

![Chatbot UI Preview](./preview.png)

---

## 🚀 Features

- 💬 Real-time AI chat using OpenRouter (GPT 3.5)
- ✨ Clean UI with Solid.js + custom CSS
- 📢 Post to Twitter clone via API using trigger phrase
- 🧠 Uses FastAPI for backend with proper CORS and environment config

---

## 📦 Project Structure

ai_chat_bot/
├── backend/
│ ├── main.py
│ ├── chat_router.py
│ ├── requirements.txt
│ ├── .env
│ └── static/ (optional - if serving frontend from backend)
├── frontend/
│ ├── src/
│ │ ├── App.jsx
│ │ ├── index.jsx
│ │ ├── lib/api.js
│ │ └── index.css
│ ├── .env
│ ├── package.json
│ └── vite.config.js
└── README.md


---

## 🔧 Prerequisites

Install the following:

- [Node.js](https://nodejs.org/) (v18+)
- [Python](https://www.python.org/downloads/) (v3.8+)
- [Git](https://git-scm.com/)

---

## 🛠️ Backend Setup (FastAPI)

### 🔹 Step 1: Create virtual environment

```bash
cd backend
python -m venv venv
# Activate venv:
# On Windows:
.\venv\Scripts\Activate.ps1
# On macOS/Linux:
source venv/bin/activate
