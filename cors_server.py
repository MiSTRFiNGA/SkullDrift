from http.server import HTTPServer, SimpleHTTPRequestHandler
import os
os.chdir(r'D:\Dev\SkullDrift')
class H(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()
HTTPServer(('127.0.0.1', 8378), H).serve_forever()
