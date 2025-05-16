import requests
import json

def handle_fallback(text):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "llama3", "prompt": f"Answer concisely: {text}", "stream": False}
    )
    return response.json().get("response", "I couldn't understand that.")
