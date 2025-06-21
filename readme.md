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

AI_CHAT_BOT/
├── backend/
│ ├── pycache/
│ ├── static/
│ │ └── index.html
│ ├── venv/
│ ├── .env
│ ├── chat_router.py
│ ├── main.py
│ └── requirements.txt
├── frontend/
│ ├── node_modules/
│ ├── .env
│ ├── index.html
│ ├── index.css
│ ├── package.json
│ ├── vite.config.js
│ └── src/
│ ├── assets/
│ ├── lib/
│ │ └── api.js
│ ├── App.jsx
│ └── index.jsx
├── README.md
└── .gitignore


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
