
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import os
import uuid
import os.path
import json

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

def root_handler(handler):
    handler.send_response(200)
    handler.send_header("Content-Type", "text/html")
    handler.end_headers()
    handler.wfile.write(bytes(htmlPage, "utf-8"))

def get_container_id_handler(handler):
    handler.send_response(200)
    handler.send_header("Content-Type", "application/json")
    handler.end_headers()
    response = {"containerId": container_id}
    handler.wfile.write(json.dumps(response).encode("utf-8"))

class MyServer(BaseHTTPRequestHandler):
    routes = {
        "/": root_handler,
        "/getContainerId": get_container_id_handler,
    }
    
    def do_GET(self):
        handler_function = self.routes.get(self.path, self.not_found_handler)
        handler_function(self)

    def not_found_handler(self):
        self.send_response(404)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"404 Not Found")
if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
    print("Server stopped ...")
