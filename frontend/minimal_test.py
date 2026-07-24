import http.server, os
os.chdir("D:\\Git\\frontend\\dist")
http.server.HTTPServer(("0.0.0.0", 5173), http.server.SimpleHTTPRequestHandler).serve_forever()