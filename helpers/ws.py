#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests, requests.cookies, json
from websocket import create_connection

#ip = sys.argv[1]
ip = '192.168.0.100' + ':9090'
url = 'ws://{}/api/ws'.format(ip)

ws = create_connection(url, timeout=5)
ws.recv()

data = json.dumps({'action': 'get_cookies', 'data': '*'})
ws.send(data)

response = json.loads(ws.recv())