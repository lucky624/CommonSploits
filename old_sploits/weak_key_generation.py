#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json, uuid, re, base64
from websocket import create_connection
from Crypto.Cipher import DES

url = 'ws://localhost/api/ws'



username = uuid.uuid4().hex
data = json.dumps({'action': 'get_my_comments', 'data': 'ker'})
while True:
    ws = create_connection(url, timeout=5)
    ws.recv()
    ws.send(data)
    response = json.loads(ws.recv())
    print(response['Response'])







