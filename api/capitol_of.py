from http.server import BaseHTTPRequestHandler
from urllib import parse
# import requests


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        
        url_parts = parse.urlsplit(self.path)
        query_string = parse.parse_qsl(url_parts.query)
        dic = dict(query_string)
         
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        msg = f'{dic}'
        self.wfile.write(msg.encode())
        return
