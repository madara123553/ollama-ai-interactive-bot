import requests
import json

def query_ollama(prompt):
    prompt = f"Respond concisely in a short sentence or two: {prompt}"

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "llama3", "prompt": prompt},
            stream=True
        )

        reply = ""
        for line in response.iter_lines():
            if line:
                try:
                    data = json.loads(line.decode("utf-8"))
                    reply += data.get("response", "")
                except Exception as e:
                    print("Error parsing response chunk:", e)
        return reply
    except Exception as e:
        print("Failed to query Ollama:", e)
        return "Sorry, I couldn’t get a response from the AI."
