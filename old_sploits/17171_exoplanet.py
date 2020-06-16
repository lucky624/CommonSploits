#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, re, requests, json
import string, random, uuid

def generator(size=12, chars=string.digits + string.ascii_letters):
    return ''.join(random.choice(chars) for _ in range(size))

#ip = sys.argv[1]
ip = 'localhost' + ':17171'
url = 'http://{}'.format(ip)

s = requests.Session()

r = requests.Session()





token = "AgAAABgAAAAQAAAAac41ZTlmMDZlNzgyZjJiYzAwMDZhYzc0NTcUcYwRqzJgN8w9WR4NZK0Y"
token = "AgAAABgAAAAQAAAAac41ZTlmMDZlNzgyZjJiYzAwMDZhYzc0NTcUcYwRqzJgN8w9WR4NZK0Y"

stars = s.get(url + '/api/stars/', timeout=(None,None)).json()

for star in stars:
    #star_id = star["id"]
    star_id = "5e9f06e782f2bc0006ac7457"
    #star_info = s.get(url + '/api/stars/{}'.format(star_id), timeout=(None, None)).json()
    #print(star_info)


    add = s.post('http://farm:17171' + '/api/stars/', json={'name' : 'lucky624', 'location' : str(star_id)}, timeout=(None, None)).json()

    #star_info = s.get(url + '/api/planets/{}'.format(star_info['planets'][0]), timeout=(None, None)).json()

    #print(star_info)
    print(s.cookies.get_dict())

    break

