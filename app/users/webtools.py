#!/usr/bin/env python

import httplib, re

def validateURL(url):
    pass

class UrlParser(object):
    def __init__(self, url):
        
        self.url = url
        self.splitted = httplib.urlsplit(self.url, scheme = '', allow_fragments = True)

        if not self.splitted[0]:
            self.url = 'http://' + url
            self.splitted = httplib.urlsplit(self.url, scheme = '', allow_fragments = True)

        self.scheme = self.splitted[0]
        self.host = self.splitted[1]
        self.path = self.splitted[2]
        #self.query = self.splitted[3]
        #self.fragment = self.splitted[4]

        self.host = self.scheme + self.netloc

# class GetStatus(object):
#     """docstring for Poke"""
#     def __init__(self, host, path ="/"):
#         self.host = host
#         self.path = path
#     def pokeSite(self):
#         try:
#             conn = httplib.HTTPConnection(self.host)
#             conn.request("HEAD", self.path)
#             self.StatusCode = conn.getresponse().status
#             self.Response = httplib.responses[self.StatusCode]
#             return (self.StatusCode, self.Response)
#         except StandardError:
#             self.StatusCode = None
#             self.Response = None
#             return (self.StatusCode, self.Response)

def pokeSite(host, path = "/"):
    try:
        conn = httplib.HTTPConnection(host)
        conn.request("HEAD", path)
        statusCode = conn.getresponse().status
        response = httplib.responses[statusCode]

        return (statusCode, response)
    
    except StandardError:
        statusCode = None
        response = None

        return (statusCode, response)