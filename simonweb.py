from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostname = "localhost"
serverPort = 8080

class SimonsServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>simonsHemsida</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: webtest</p>", "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This i my first web page</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":
    webserver = HTTPServer((hostname, serverPort), SimonsServer)
    print("Server started http://{}{}".format(hostname, serverPort))

    try:
        webserver.serve_forever()
    except KeyboardInterrupt:
        pass

    webserver.server_close()
    print("Server stopped.")