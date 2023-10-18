import http.server
import socketserver

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Get the visitor's IP address
        ip_address = self.client_address[0]

        # Create a web page with the visitor's IP address
        html = """
        <!DOCTYPE html>
        <html><head><title>My Web Server</title></head>
        <body><h1>Visitor IP Address: {}</h1></body></html>
        """.format(ip_address)

        # Send the web page to the visitor
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.send_header('Content-Length', len(html))
        self.end_headers()

        self.wfile.write(html.encode('utf-8'))

if __name__ == '__main__':
    server = socketserver.TCPServer(('', 8080), MyHandler)
    server.serve_forever()