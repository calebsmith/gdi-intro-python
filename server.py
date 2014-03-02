#!/usr/bin/env python
"""
A server that works with the livereload chrome extension to automatically
refresh the browser whenver a set of files changes. The server degrades to a
SimpleHTTPServer w/o livereload capability if the livereload Python package is
not available.

The default port is 8000. Supply a commandline argument for a different port.

This serves files from the current directory on your local browser and is good
for viewing slides easily.

E.g. Links to slides for all classes can viewed by visiting:
http://localhost:8000/

on the same computer that is running the server.

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

try:
    from livereload import Server as LiveServer
except ImportError:
    LiveServer = None


DEFAULT_PORT = 8000
patterns = [
    '*.html',
    'set*/slides/*.md',
    'set*/*.html',
    'images/',
    'css/',
]


def main(port):
    if LiveServer is not None:
        live_reload_server(port)
    else:
        print("Using SimpleHTTPServer. Follow the README for livereload if "
            "desired")
        simple_server(port)


def simple_server(port):
    HandlerClass.protocol_version = Protocol
    httpd = ServerClass((SERVER_ADDRESS, port), HandlerClass)
    sa = httpd.socket.getsockname()
    print("Serving HTTP on", sa[0], "port", sa[1], "...")
    httpd.serve_forever()


def live_reload_server(port):
    server = LiveServer()
    for pattern in patterns:
        server.watch(pattern)
    server.serve(port=port)


if __name__ == '__main__':
    port = int(sys.argv[1]) if sys.argv[1:] else 8000
    main(port)
