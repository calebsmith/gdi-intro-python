#!/usr/bin/env python

from livereload import Server

DEFAULT_PORT = 8000
patterns = [
    '*.md',
    '*.html',
    '/images',
    '/css',
]

server = Server()
for pattern in patterns:
    server.watch(pattern)
server.serve(port=DEFAULT_PORT)
