#!/bin/python3
import http.server
import short_url

id = 20  # your object id
domain = 'mytiny.domain' 

shortened_url = "http://{}/{}".format(
                                     domain,
                                     short_url.encode_url(id)
                               )
print(shortened_url)

def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()