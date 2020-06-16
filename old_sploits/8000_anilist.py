#!/usr/bin/env python
# -*- coding: utf-8 -*-
from storage import storage_set, storage_get
import sys, re, requests
import string, random, uuid, re, json

#ip = sys.argv[1]
ip = sys.argv[1]

s = requests.Session()

def generator(size=12, chars=string.digits + string.ascii_letters):
    return ''.join(random.choice(chars) for _ in range(size))

username = generator()
password = generator()

auth = {"name":username,"password":password}
html = s.post('http://{}:8000/api/auth/register'.format(ip),json=auth,timeout=(None,None))
html = s.post('http://{}:8000/api/auth/login'.format(ip),json=auth,timeout=(None,None))


for i in range(0,1000):
    if not storage_get(ip + ':' + 'new_count' + str(i)):
        try:
            html = s.get('http://{}:8000/api/db/anime/{}'.format(ip, i),timeout=(None,None))
        except:
            break
        try:
            print(re.search('[A-Z0-9]{31}=', html.text).group(0))
            storage_set(ip + ':' + 'new_count' + str(i))
        except:
            pass



#users = json.loads(s.get('http://{}:8000/api/chat/users/'.format(ip)).text)

#for user in users['result']:
#    print(user)
#    break