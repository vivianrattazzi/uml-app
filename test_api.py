import requests

response = requests.post(
    "http://127.0.0.1:8080/v1/chat/completions",
    json={
        "messages": [
            {
                "role": "user",
                "content": "Chi sei?"
            }
        ],
        "temperature": 0.1,
        "max_tokens": 50
    }
)

print(response.json()["choices"][0]["message"]["content"])