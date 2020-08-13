#coding: utf-8


import http.server


port =80
address=("", port)
server = http.server.HTTPServer

handler = http.server.CGIHTTPRequestHandler

handler.cgi_directories = ["/"]
httpd = server(address, handler)


print(httpd)
print(f"serveur au  http://127.0.0.1:{port}")
httpd.serve_forever()

