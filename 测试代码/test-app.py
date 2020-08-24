# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 17:24:08 2020
web test
pip install web.py==0.40.dev0
##创建
@author: HP

"""
import web
import json
URLS =("/test","TestPlus") ##test 映射到TestPlus方法 
class TestPlus(object):   ##类必须是大写
    def GET(self):     ##GET()大写
        ##GET方法 用 web.input 获取
        data = web.input()
        if "a" in data and "b" in data:
            a = data.get("a")
            b = data.get("b")
            return "a+b={}".format(a+b)
        else:
           return "This is Test,not fund a or b!"
    def POST(self):
        ##POST方法 用 web.data 获取
        data = web.data()
        print(data)
        data = json.loads(data)
        if "a" in data and "b" in data:
            a = data.get("a")
            b = data.get("b")
            return "a+b={}".format(a+b)
        else:
           return "This is Test,not fund a or b!"
   

if __name__=='__main__':
    app = web.application(URLS,globals())
    app.run()
    