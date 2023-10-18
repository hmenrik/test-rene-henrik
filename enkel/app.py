import http.server
import socketserver

PORT = 80

Handler = http.server.SimpleHTTPRequestHandler

def serve_forever():
    while True:
        client, addr = server.accept()
        Handler(client, addr).handle()

if __name__ == "__main__":
    server = http.server.HTTPServer(("", PORT), Handler)
    print("Serving at port", PORT)
    serve_forever()