import http.server, os, io
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "dist"))

class CustomHandler(http.server.BaseHTTPRequestHandler):
    def _serve_file(self, filepath):
        try:
            with open(filepath, "rb") as f:
                content = f.read()
        except:
            self.send_error(404)
            return
        ct = "text/html" if filepath.endswith(".html") else "application/octet-stream"
        if filepath.endswith(".css"): ct = "text/css"
        if filepath.endswith(".js"): ct = "application/javascript"
        if filepath.endswith((".jpg",".jpeg")): ct = "image/jpeg"
        if filepath.endswith(".png"): ct = "image/png"
        if filepath.endswith(".svg"): ct = "image/svg+xml"
        if filepath.endswith(".woff"): ct = "font/woff"
        if filepath.endswith(".woff2"): ct = "font/woff2"
        if filepath.endswith((".ico","gif","webp")): ct = "image/webp"
        self.send_response(200)
        self.send_header("Content-type", ct)
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)

    def do_GET(self):
        # Map URL path to filesystem path
        path = self.path.split("?")[0].split("#")[0]
        if path == "/" or path == "":
            path = "/index.html"
        filepath = os.getcwd() + path.replace("/", os.sep)
        if os.path.exists(filepath) and not os.path.isdir(filepath):
            self._serve_file(filepath)
        else:
            # SPA fallback: serve index.html
            self._serve_file(os.path.join(os.getcwd(), "index.html"))

http.server.HTTPServer(("0.0.0.0", 5173), CustomHandler).serve_forever()