#!/usr/bin/env python
import sys

__doc__ = """
Very simple HTTP server in python.

Usage:
        %s  <port>


Send a GET request:
    curl http://localhost

Send a HEAD request:
    curl -I http://localhost

Send a POST request:
    curl -d "foo=bar&bin=baz" http://localhost

"""%(sys.argv[0])

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write("<html><body><h1>hi!</h1></body></html>")

    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self,fileout=None):
        ## Write down posted data 
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        if fileout != None:
            with open('post_content.txt','w') as fp:
                fp.write(post_data)
        else:
            print('--- POST content ---')
            print(post_data)
            print('--- ---')
        self._set_headers()


def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        run(port=int(sys.argv[1]))
    else:
        print __doc__
