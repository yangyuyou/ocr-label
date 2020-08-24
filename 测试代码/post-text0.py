# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 22:01:15 2020

@author: HP
"""


import requests
import json

def get():
    url="http://127.0.0.1:8080/test1?a=6&b=djdjdjd6"
    req=requests.get(url)
    print(req.text)
def post():
    url="http://127.0.0.1:8080/test1"
    data={"a":"3534534","b":"ksalf"}
    req=requests.post(url,data=json.dumps(data))
    print(req.text)
if __name__=='__main__':
    post()
     