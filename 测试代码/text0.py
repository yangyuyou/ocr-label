# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 21:17:40 2020

@author: HP
"""


import web
import json

URLS=("/test1","TestPlus")
class TestPlus(object):
    def GET(self):
        data=web.input()
        if "a" in data and "b" in data:
            a=data.get("a")
            b=data.get("b")
            return "a+b={}".format(a+b)
        else:
            return "This is Test,not found a and b"
    def POST(self):
        data=web.data()
        data=json.loads(data)
        if "a" in data and "b" in data:
            a=data.get("a")
            b=data.get("b")
            return "a+b={}".format(a+b)
        else:
            return "This is Test,not found a and b"
if __name__=='__main__':
    app=web.application(URLS,globals())
    app.run()