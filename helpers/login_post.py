#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, re, requests

#ip = sys.argv[1]
ip = '192.168.0.104'

auth_data = {
    'login': 'bee',
    'password' : 'bug',
    'security_level' : '0',
    'form' : 'submit'
}


s = requests.Session()

html = s.post('http://{}/bWAPP/login.php'.format(ip), data=auth_data)
print(html.text)