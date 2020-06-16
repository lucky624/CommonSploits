#!/usr/bin/env python
# -*- coding: utf-8 -*-
from storage import storage_set, storage_get
import sys, requests
import string, random, re, json

#ip = sys.argv[1]
ip = '10.70.60.2' + ':8000'

s = requests.Session()

def generator(size=12, chars=string.digits + string.ascii_letters):
    return ''.join(random.choice(chars) for _ in range(size))

username = generator()
password = generator()

auth = {"name":username,"password":password}

html = s.post('http://{}/api/auth/login'.format(ip),json=auth,timeout=(None,None))

def register_user(s):
    s.post('http://{}/api/auth/register'.format(ip), json=auth, timeout=(None, None))
    return s

def login_user(s):
    s.post('http://{}/api/auth/login'.format(ip), json=auth, timeout=(None, None))
    return s

def get_users(s):
    users = json.loads(s.get('http://{}/api/chat/users/'.format(ip),timeout=(None,None)).text)
    return users

def send_msg(s,user):
    data = {"message": "omaviat_gang","to": user}
    s.post('http://{}/api/chat/enter/'.format(ip))
    html = s.post('http://{}/api/chat/send_messages/'.format(ip),json=data,timeout=(None,None)).text
    print(html)
    return s


def get_msg(s,user):
    s.post('http://{}/api/chat/enter/'.format(ip),timeout=(None,None))
    data = {"to": user, "from": {"$ne": "null"}}
    html = s.post('http://{}/api/chat/get_messages/'.format(ip),json=data,timeout=(None,None)).text
    print(re.findall('[A-Z0-9]{31}=', html),flush=True)
    return s



if __name__ == '__main__':
    register_user(s)
    login_user(s)
    users = get_users(s)
    for user in users['result']:
        if not storage_get(ip + ':' + user['name']):
            get_msg(s,user['name'])
            storage_set(ip + ':' + user['name'])





