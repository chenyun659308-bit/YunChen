import http.server, os, io

os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "dist"))

handler = http.server.SimpleHTTPRequestHandler
_old_send = handler.send_head

def _new_send(self):
    path = self.translate_path(self.path)
    if not os.path.exists(path) or os.path.isdir(path):
        # SPA fallback: serve dist/index.html directly
        self.path = "/index.html"
        path = os.path.join(os.getcwd(), "index.html")
        content = open(path, "rb").read()
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        return io.BytesIO(content)
    return _old_send(self)

handler.send_head = _new_send

http.server.HTTPServer(("0.0.0.0", 5173), handler).serve_forever()