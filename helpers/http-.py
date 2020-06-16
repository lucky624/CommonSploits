#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, re, requests
import string, random, uuid

def generator(size=12, chars=string.digits + string.ascii_letters):
    return ''.join(random.choice(chars) for _ in range(size))

#ip = sys.argv[1]
ip = '192.168.0.100' + ':9090'
url = 'http://{}'.format(ip)

s = requests.Session()

#s.post(url + '', timeout=(None,None))
#s.get(url + '', timeout=(None,None))

