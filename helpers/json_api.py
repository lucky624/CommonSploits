#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, re, requests,json

#ip = sys.argv[1]
auth_url = 'https://api.random.org/json-rpc/2/invoke'
headers = {'Content-Type':'application/json'}

auth = {
    "jsonrpc": "2.0",
    "method": "generateIntegers",
    "params": {
        "apiKey": "5bba64e6-74fb-42cc-af6e-880f519506f1",
        "n": 6,
        "min": 1,
        "max": 6,
        "replacement": True
    },
    "id": 42
}

with requests.Session() as s:
    html = s.post(auth_url, headers=headers, json = auth)
    print(html.json()['result']['random']['data'])