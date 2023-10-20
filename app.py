import http.server
import socketserver
from urllib import request
#asd
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Get the visitor's IP address. ändra till att läsa x-forwarded for
        ip_address = self.client_address[0]
        
        # for header in self.headers:
        #     print(header)
        ip_reneaddress = request.headers.get("x-forwarded-for", request.remote_addr)
            
            
        # Create a web page with the visitor's IP address
        html = """
        <!DOCTYPE html>
        <html><head><title>ip.stg.int</title><meta charset="utf-8"></head>
        <body><h1>Din IP-adress är: {}</h1>
        </body></html>
        """.format(ip_reneaddress)

        # Send the web page to the visitor
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.send_header('Content-Length', len(html))
        self.end_headers()

        self.wfile.write(html.encode('utf-8'))

if __name__ == '__main__':
    server = socketserver.TCPServer(('', 8080), MyHandler)
    server.serve_forever()