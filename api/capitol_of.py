from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        
        url_parts = parse.urlsplit(self.path)
        query_string = parse.parse_qsl(url_parts.query)
        dic = dict(query_string)
        country = dic.get('country')
        capital = dic.get('capital')
        
        if 'name' in dic:
            url = 'https://restcountries.com/v3.1/name/'
            print('first url: ', url)
            full_url = url + dic['name']
            print('full url',full_url)
            request = requests.get(full_url)
            print('my request: ',request)
            data = request.json()
            print(data)
            capitol = data[0]['capital']
            print(capitol)
            msg = str(capitol)
            print(msg)
            # print("should be capitol: ", msg)
            mssg ='test'   
            self.send_response(200)
            self.send_header('Content-type','text/plain')
            self.end_headers()
            self.wfile.write(mssg.encode())
            return
