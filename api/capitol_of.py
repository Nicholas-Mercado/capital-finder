from http.server import BaseHTTPRequestHandler
# from urllib import parse
# import requests


class handler(BaseHTTPRequestHandler):
    def do_GET(self):

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        message = 'I am alive!'
        self.wfile.write(message.encode())
        return
