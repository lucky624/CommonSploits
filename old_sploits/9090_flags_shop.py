#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, re, requests
import string, random, uuid

def generator(size=12, chars=string.digits + string.ascii_letters):
    return ''.join(random.choice(chars) for _ in range(size))

username = generator()
password = generator()

#ip = sys.argv[1]
ip = '192.168.0.100' + ':9090'
url = 'http://{}'.format(ip)

s = requests.Session()

auth_data = {'username' : username, 'password' : password}

s.post(url + '/api/register', json=auth_data, timeout=(None,None))
s.post(url + '/api/login', json=auth_data, timeout=(None,None))

user = s.get(url + '/api/get_user', timeout=(None,None)).text

print(user)

