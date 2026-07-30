import http.server
import urllib.parse
import json
import os
from datetime import datetime

class FormHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/send':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = urllib.parse.parse_qs(post_data.decode('utf-8'))
            name = data.get('name', [''])[0]
            phone = data.get('phone', [''])[0]
            message = data.get('message', [''])[0]
            print(f"✅ Заявка от {name}, {phone}")
            self.send_response(302)
            self.send_header('Location', '/index.html?sent=ok')
            self.end_headers()
        
        elif self.path == '/save-lead':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            lead = data.get('lead', '')
            with open('leads.txt', 'a', encoding='utf-8') as f:
                f.write(lead)
            print(f"📝 Лид сохранён: {lead.strip()}")
            self.send_response(200)
            self.end_headers()
        
        else:
            self.send_response(404)
            self.end_headers()

    def do_GET(self):
        super().do_GET()

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    server = http.server.HTTPServer(('0.0.0.0', 8000), FormHandler)
    print("Сервер запущен: http://localhost:8000")
    server.serve_forever()