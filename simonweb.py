from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostname = "localhost"
serverPort = 8080

class SimonsServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        with open("index.html", "r") as f:
            html = f.read()
        self.wfile.write(html.encode())

if __name__ == "__main__":
    webserver = HTTPServer((hostname, serverPort), SimonsServer)
    print("Server started http://{}:{}".format(hostname, serverPort))

    try:
        webserver.serve_forever()
    except KeyboardInterrupt:
        pass

    webserver.server_close()
    print("Server stopped.")