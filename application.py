
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import os
import uuid
import os.path

hostName = "0.0.0.0"
serverPort = 8080

utfConst = "utf-8"

def get_container_id(): 
    file = "./container-uuid.txt"    
    if os.path.exists(file):
        with open(file, "r") as reader:
            return reader.read().strip()
    else :
        generated_uuid = uuid.uuid4()
        with open(file, "w") as writer:
            writer.write(str(generated_uuid))
        return str(generated_uuid)

container_id = get_container_id()

htmlPage = f"""<html><head><title>Test page docker</title></head><body><h1>This is start page</h1><p>Container identifer: {container_id}</p></body></html>"""

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(htmlPage, utfConst))
if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
    print("Server stopped ...")
