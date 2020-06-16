#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, re, requests, random, string

def generator(size=12, chars=string.digits + string.ascii_letters):
    return ''.join(random.choice(chars) for _ in range(size))

#ip = sys.argv[1]
ip = '10.70.36.2' + ':8080'

name = generator()
username = generator()
password = generator()

auth_data = {'name': name, 'username': username, 'password': password}


s = requests.Session()


html = s.options('http://{}/register'.format(ip), data=auth_data)
print(html.text)
