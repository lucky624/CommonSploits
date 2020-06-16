#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from storage import storage_set, storage_get
import sys, re, requests
import string, random, uuid

def generator(size=12, chars=string.digits + string.ascii_letters):
    return ''.join(random.choice(chars) for _ in range(size))

ip = 'farm' + ':5001'
url = 'http://{}'.format(ip)

s = requests.Session()

users = s.get(url + '/tm/health', timeout=(None,None)).json()

data = {"angle": 0, "focus": 0}
for user in users['stats']:
    jsonResponse = s.post(url + '/beam/' + user, json=data, timeout=(None, None)).text
    print(jsonResponse, flush=True)
