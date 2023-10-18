import http.server
import socketserver

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        self.wfile.write(b'<!DOCTYPE html>')
        self.wfile.write(b'<html><head><title>My Web Server</title></head>')
        self.wfile.write(b'<body><h1>Visitor IP Address: {}</h1></body></html>'.format(self.client_address[0].encode()))

if __name__ == '__app__':
    server = socketserver.TCPServer(('localhost', 80), MyHandler)
    server.serve_forever()