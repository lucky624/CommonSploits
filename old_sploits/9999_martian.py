#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os,re
os.environ['PWNLIB_NOTERM'] = 'True'
from pwn import *

#ip = sys.argv[1]
ip = 'vulnbox'
port = 9999

r = remote(ip, port)