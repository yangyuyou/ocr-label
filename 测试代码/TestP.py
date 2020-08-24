# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 15:15:03 2020

@author: HP
"""


import web
import json

URLS=("/label","TestP")

class TestP(object):
    def GET(self):
        data=web.input()
        if "a" in data and "b" in data:            
            a=int(data.get("a"))
            b=int(data.get("b"))
            return "a+b={}".format(a+b)
        else:
            return "This is a Test,not found a and b"
    def POST(self):
        data=web.data()
        data=json.loads(data)
        if "a" in data and "b" in data:            
            a=int(data.get("a"))
            b=int(data.get("b"))
            return "a+b={}".format(a+b)
        else:
            return "This is a Test,not found a and b"
if __name__=='__main__':
    app=web.application(URLS,globals())
    app.run()
        
    