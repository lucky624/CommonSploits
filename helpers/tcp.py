#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os,re
os.environ['PWNLIB_NOTERM'] = 'True'
from pwn import *

#ip = sys.argv[1]
ip = '10.0.8.5'
port = 3333

r = remote(ip, port)

#r.recvuntil('You are welcome !')
#r.recvrepeat(timeout=1)

#r.sendline('1')


r.close()


