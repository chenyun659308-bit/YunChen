@echo off
start "Frontend" /MIN /D D:\Git\frontend D:\Git\.venv\Scripts\python.exe -c "import http.server, os; os.chdir('D:\Git\frontend\dist'); http.server.HTTPServer(('0.0.0.0', 5173), http.server.SimpleHTTPRequestHandler).serve_forever()"
echo Frontend started on :5173