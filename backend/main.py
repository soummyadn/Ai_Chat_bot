from dotenv import load_dotenv
load_dotenv()    # still OK here, but chat_router already loaded .env

import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from chat_router import router as chat_router

app = FastAPI(title="AI Chatbot Backend")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# mount chat router
app.include_router(chat_router)

# health‑check endpoint
@app.get("/")
async def read_root():
    return {"status": "ok", "message": "AI Chatbot backend is up. POST to /chat/"}

# (optional) serve frontend build
app.mount("/", StaticFiles(directory="static", html=True), name="static")
