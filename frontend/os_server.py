import http.server, os, io

os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "dist"))

class OS(http.server.BaseHTTPRequestHandler):
    def _read(self, path):
        fd = os.open(path, os.O_RDONLY | os.O_BINARY)
        sz = os.fstat(fd).st_size
        data = os.read(fd, sz)
        os.close(fd)
        return data

    def _ct(self, path):
        if path.endswith('.html'): return 'text/html; charset=utf-8'
        if path.endswith('.css'): return 'text/css; charset=utf-8'
        if path.endswith('.js'): return 'application/javascript; charset=utf-8'
        if path.endswith(('.jpg','.jpeg')): return 'image/jpeg'
        if path.endswith('.png'): return 'image/png'
        if path.endswith('.svg'): return 'image/svg+xml'
        if path.endswith(('.woff','.woff2')): return 'font/woff2'
        if path.endswith(('.ico','gif','webp')): return 'image/webp'
        return 'application/octet-stream'

    def send(self, data, ct):
        self.send_response(200)
        self.send_header('Content-type', ct)
        self.send_header('Content-Length', str(len(data)))
        self.end_headers()
        return io.BytesIO(data)

    def do_GET(self):
        p = self.path.split('?')[0].split('#')[0]
        if p == '/' or p == '':
            p = '/index.html'
        fp = os.getcwd() + p.replace('/', os.sep)
        if os.path.exists(fp) and not os.path.isdir(fp):
            data = self._read(fp)
            self.copyfile(self.send(data, self._ct(fp)), self.wfile)
        else:
            data = self._read(os.path.join(os.getcwd(), 'index.html'))
            self.copyfile(self.send(data, 'text/html; charset=utf-8'), self.wfile)

OS.protocol_version = 'HTTP/1.0'
http.server.HTTPServer(('0.0.0.0', 5173), OS).serve_forever()