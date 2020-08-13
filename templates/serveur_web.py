#coding: utf-8


import http.server
import socketserver

port =80
address=("", port)

handler = http.server.CGIHTTPRequestHandler

handler.cgi_directories = ["/"]
httpd = socketserver.TCPServer(address, handler)
print(f"serveur au  http://127.0.0.1:{port}")
httpd.serve_forever()

