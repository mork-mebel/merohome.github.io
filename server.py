import http.server
import urllib.parse
import webbrowser
import os
from datetime import datetime

YOUR_PHONE = "79035571945"  # ← Замените на ваш номер

class FormHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/send':
            try:
                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length)
                data = urllib.parse.parse_qs(post_data.decode('utf-8'))
                
                name = data.get('name', [''])[0]
                phone = data.get('phone', [''])[0]
                message = data.get('message', [''])[0]
                
                # Сохраняем заявку
                now = datetime.now().strftime("%d.%m.%Y %H:%M")
                with open('orders.txt', 'a', encoding='utf-8') as f:
                    f.write(f"\n{'='*40}\nДата: {now}\nИмя: {name}\nТелефон: {phone}\nСообщение: {message}\n")
                
                print(f"✅ Заявка от {name}, {phone}")
                
                # WhatsApp ссылка
                wa_text = f"Новая заявка Mero!\n\nИмя: {name}\nТелефон: {phone}\nСообщение: {message}"
                wa_url = f"https://wa.me/{YOUR_PHONE}?text={urllib.parse.quote(wa_text)}"
                
                # Ответ с открытием WhatsApp
                html = f"""<!DOCTYPE html>
                <html><head><meta charset="UTF-8"></head>
                <body style="text-align:center;padding:50px;font-family:Arial;">
                <h2>Заявка отправлена!</h2>
                <p>Мы свяжемся с вами.</p>
                <a href="/index.html">← Вернуться на сайт</a>
                <script>window.open('{wa_url}', '_blank');</script>
                </body></html>"""
                
                self.send_response(200)
                self.send_header('Content-type', 'text/html; charset=utf-8')
                self.end_headers()
                self.wfile.write(html.encode())
            except Exception as e:
                print(f"Ошибка: {e}")

    def do_GET(self):
        super().do_GET()

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    server = http.server.HTTPServer(('0.0.0.0', 8000), FormHandler)
    print("Сервер запущен: http://localhost:8000")
    server.serve_forever()