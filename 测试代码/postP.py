# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 15:48:23 2020

@author: HP
"""

import requests
import json
def get():
    url="http://127.0.0.1:8080/label?a=1&b=3"
    req=requests.get(url)
    print(req.text)

def post():
    url="http://127.0.0.1:8080/label"
    data={"a":"1","b":"2"}
    req=requests.post(url,data=json.dumps(data))
    print(req.text)
if __name__=='__main__':
    post()
