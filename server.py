from http.server import HTTPServer, BaseHTTPRequestHandler
from uuid import uuid4
import ssl

PORT = 8083
SSL = False

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.mirror()

    def do_POST(self):
        self.mirror()
    
    def do_PUT(self):
        self.mirror()

    def do_HEAD(self):
        self.mirror()

    def mirror(self):
        self.send_response(200)
        self.send_header('Set-Cookie', f"session={uuid4()}; SameSite=None;")
        self.end_headers()
        self.wfile.write(b'\n==> Request line:\n')
        self.wfile.write(bytes(self.requestline + '\n', 'UTF-8'))            
        self.wfile.write(b'\n==> Headers:\n')
        self.wfile.write(self.headers.as_bytes())
        if (self.command == "POST" or self.command == "PUT"):                
            cl = self.headers.get("Content-Length")
            if cl != "" and cl != None and int(cl) != 0:
                self.wfile.write(b'\n==> Body:\n')
                self.wfile.write(self.rfile.read(int(cl)))
        
        self.wfile.write(b'\n')
    
server1 = HTTPServer(('', PORT), SimpleHTTPRequestHandler)

if SSL:
    server1.socket = ssl.wrap_socket (server1.socket,
            keyfile='./demokey.pem',
            certfile='./democert.pem', server_side=True)


try:    
    server1.serve_forever()
except KeyboardInterrupt:    
    print("\nShutting down...")
    server1.socket.close()

