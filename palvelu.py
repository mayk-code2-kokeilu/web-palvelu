# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 11:47:39 2025

@author: Panu.Kalliokoski
"""

from wsgiref.simple_server import make_server

def app(environ, respond):
    respond('200 OK', [('Content-type', 'text/html; charset=utf-8')])
    yield "Hello w€rld😞!".encode('utf-8')
    polku = environ["PATH_INFO"]
    salanimi = polku.replace("a", "aca").replace("i", "hani").replace("n", "nono")
    yield "<p>moikka</p>".encode('utf-8')
    yield (f"Salainen nimesi on: <b>{salanimi}</b>".encode('utf-8'))
    #for key in environ:
    #    yield ("%s: %s\n" % (key, environ[key])).encode('utf-8')


if __name__ == '__main__':
    with make_server("localhost", 8000, app) as server: 
        server.serve_forever()
