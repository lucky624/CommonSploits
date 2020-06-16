#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, re, requests, random, string
from storage import storage_set, storage_get

def generator(size=12, chars=string.digits + string.ascii_letters):
    return ''.join(random.choice(chars) for _ in range(size))

#ip = sys.argv[1]
ip = '10.70.36.2' + ':4000'


username = generator()
password = generator()

auth_data = {'login': username, 'password': password}

s = requests.Session()

html = s.post('http://{}/register'.format(ip), data=auth_data,timeout=(None,None))
#print(html.cookies)
html = s.post('http://{}/login'.format(ip), data=auth_data,timeout=(None,None))
html = s.get('http://{}/home'.format(ip), timeout=(None,None))
print(html.text)






s.close()