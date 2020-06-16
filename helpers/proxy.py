#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, re, requests

#ip = sys.argv[1]
ip = '192.168.0.104'

#Burp --> Proxy --> Intercept --> Intercept is off

proxies = {
  'http': 'http://127.0.0.1:8080',
  'https': 'http://127.0.0.1:8080',
}

auth_data = {
    'login': 'bee',
    'password' : 'bug',
    'security_level' : '0',
    'form' : 'submit'
}

with requests.Session() as s:
    html = s.post('http://{}/bWAPP/login.php'.format(ip), data=auth_data, proxies=proxies)
    print(html.text)