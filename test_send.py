import urllib.request
import json

BOT_TOKEN = "8715161032:AAFCUgcYLJbDGjjCk6DrE0cGmlQgVBa1D_8"
CHAT_ID = "261458452"

text = "🧪 Тестовое сообщение от Mero!\nФорма работает!"

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
payload = json.dumps({
    'chat_id': CHAT_ID,
    'text': text
}).encode('utf-8')

req = urllib.request.Request(url, data=payload, headers={'Content-Type': 'application/json'})
response = urllib.request.urlopen(req)
print(f"Статус: {response.status}")
print(f"Ответ: {response.read().decode()}")
print("✅ Если статус 200 — Telegram работает!")