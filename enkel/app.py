import http.server
import threading

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

def serve_forever():
    while True:
        client, addr = server.accept()
        Handler(client, addr).handle()

if __name__ == "__main__":
    server = http.server.HTTPServer(("", PORT), Handler)
    print("Serving at port", PORT)
    threading.Thread(target=serve_forever).start()
    server.serve_forever()