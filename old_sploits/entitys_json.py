#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import sys, re, requests

url = 'https://5.enowars.com/api/attackinfo'

s = requests.Session()

jsonResp = s.get(url, timeout=(None,None)).json()

ips =  jsonResp['services']['stldoctor']


exit(0)
ips_dict = dict(ips)

for item in ips_dict:
    for round in ips_dict[item]:
        entitys = ips_dict[item]
        print(entitys[round])
        try:
            first = entitys[round]['0']
            second = entitys[round]['1']
            print(first + '  ' + second)
        except:
            continue








