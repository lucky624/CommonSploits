#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, re, requests,json

auth_url = 'http://127.0.0.1/api/login'
headers = {'Content-Type':'application/json'}

auth = {
    'username': 'adminn',
    'password' : 'admin'
}

with requests.Session() as s:
    html = s.post(auth_url, headers=headers, json = auth)
    print(html.text)
    html = s.get('http://127.0.0.1/api/logout')
    print(html.text)