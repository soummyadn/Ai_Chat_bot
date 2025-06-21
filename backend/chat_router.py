# backend/chat_router.py

# 1) Load .env immediately
from dotenv import load_dotenv
load_dotenv()

import os
import requests
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import openai

# 2) OpenRouter setup
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
if not OPENROUTER_API_KEY:
    raise RuntimeError("OPENROUTER_API_KEY not set in environment")

client = openai.OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

# 3) Twitter‑clone API setup
TWITTER_CLONE_URL = "https://twitterclone-server-2xz2.onrender.com/post_tweet"
TWITTER_CLONE_KEY = os.getenv("TWITTER_CLONE_API_KEY")
if not TWITTER_CLONE_KEY:
    raise RuntimeError("TWITTER_CLONE_API_KEY not set in environment")

router = APIRouter(prefix="/chat")

class ChatRequest(BaseModel):
    message: str

@router.post("/")
async def chat_endpoint(req: ChatRequest):
    text = req.message.strip()
    lower = text.lower()

    # 1️⃣ If user asked to post to twitter:
    if lower.startswith("post to twitter:"):
        content = text.split(":", 1)[1].strip()
        if not content:
            raise HTTPException(status_code=400, detail="No tweet text provided.")

        # Build payload
        payload = {
            "username": "soummyadeep",  # or pull from env if dynamic
            "text": content
        }
        headers = {
            "api-key": TWITTER_CLONE_KEY,
            "Content-Type": "application/json"
        }

        # Send to clone API
        resp = requests.post(TWITTER_CLONE_URL, json=payload, headers=headers)
        if resp.status_code != 200:
            raise HTTPException(
                status_code=502,
                detail=f"Twitter‑clone API error: {resp.status_code} {resp.text}"
            )

        # Return a confirmation
        return {"reply": f"✅ Your tweet was posted: \"{content}\""}

    # 2️⃣ Otherwise use OpenRouter for chat
    try:
        resp = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": text}],
        )
    except Exception as e:
        print(f"[chat_router] OpenRouter error: {e!r}")
        raise HTTPException(status_code=502, detail=str(e))

    reply = resp.choices[0].message.content
    return {"reply": reply}
