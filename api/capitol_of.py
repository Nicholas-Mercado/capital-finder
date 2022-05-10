from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        
        url_parts = parse.urlsplit(self.path)
        query_string = parse.parse_qsl(url_parts.query)
        dic = dict(query_string)
        country = dic.get('name')
        capital = dic.get('capital')
        
        if country:
            url = 'https://restcountries.com/v3.1/name/'
            full_url = url + dic['name']
            request = requests.get(full_url)
            data = request.json()
            capital = str(data[0]['capital'][0])
            
            msg = f'The capital of {country} is {capital}' 
            self.send_response(200)
            self.send_header('Content-type','text/plain')
            self.end_headers()
            self.wfile.write(msg.encode())
            return

