# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 17:39:26 2020
python 程序调用网页
@author: HP
"""
import requests
import json
def get():
    ##get 请求
   url  = "http://127.0.0.1:8080/test?a=10&b=23322"
   req = requests.get(url)
   print(req.text)
   
def post():
    url  = "http://127.0.0.1:8080/test"
   
    data = {'a':'33333232','b':'djd384843j'}
    req = requests.post(url, data=json.dumps(data))
   
    print(req.text) 

if __name__=='__main__':
    post()

