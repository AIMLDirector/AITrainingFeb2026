import requests

url = "http://localhost:1234/v1/chat/completions"

payload = {
    "model": "gemma-3-4b-it-qat",
    "messages": [{"role": "user", "content": "Hello"}]
}

response = requests.post(url, json=payload)
print(response.json()["choices"][0]["message"]["content"])