#!/usr/bin/python
"""
A simple server that serves only on the localhost.

Default port is 8000. Supply a commandline argument for a different port.

This serves files from the current directory on your local browser and is good
for viewing slides easily.

E.g. Links to slides for all classes can viewed by visiting:
http://localhost:8000/

on the same computer that is running the server

Usage:

python server.py

or

python server.py <port>
"""

import sys
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

HandlerClass = SimpleHTTPRequestHandler
ServerClass = BaseHTTPServer.HTTPServer
Protocol = "HTTP/1.0"

SERVER_ADDRESS = '127.0.0.1'


def main(port):
    HandlerClass.protocol_version = Protocol
    httpd = ServerClass((SERVER_ADDRESS, port), HandlerClass)
    sa = httpd.socket.getsockname()
    print "Serving HTTP on", sa[0], "port", sa[1], "..."
    httpd.serve_forever()


if __name__ == '__main__':
    port = int(sys.argv[1]) if sys.argv[1:] else 8000
    main(port)

