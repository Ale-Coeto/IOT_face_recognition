from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.get('/')
def hello_world():
    return "Hello, World!"

# from http.server import BaseHTTPRequestHandler
 
# class handler(BaseHTTPRequestHandler):
 
#     def do_GET(self):
#         self.send_response(200)
#         self.send_header('Content-type','text/plain')
#         self.end_headers()
#         self.wfile.write('Hello, world!'.encode('utf-8'))
#         return
