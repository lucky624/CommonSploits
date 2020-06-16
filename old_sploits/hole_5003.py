#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os,re
os.environ['PWNLIB_NOTERM'] = 'True'
from pwn import *

#ip = sys.argv[1]
ip = '192.168.0.100'
port = 5003

r = remote(ip, port)

def generator(size=12, chars=string.digits + string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))

username = generator()
password = username
nik = username


def register_user(r):
    r.recvuntil('To call help send /HELP')
    r.sendline('/CREATE {} {} {}'.format(username, password, nik))
    return r

def list_users(r):
    r.sendline('/LIST')
    user_list = r.recvrepeat(timeout=1).decode()
    users = user_list.split('\n')
    users.remove('')
    users.remove('')
    users.remove('Success: User successfully created.')
    return list(users)

def login_user(r,username,password):
    r.sendline('/USER {}'.format(username))
    r.recvuntil('Success: Username found. Enter password for identifying(/PASS <pass>).')
    r.sendline('/PASS {}'.format(password))
    print(r.recvrepeat(timeout=1).decode())
    return r

def send_msg(r,msg,to,private=True):
    if private:
        r.sendline('/MSG private {} {}'.format(to,msg))
    else:
        r.sendline('/MSG public {} {}'.format(to, msg))
    print(r.recvrepeat(timeout=1).decode())
    return r

def restore_msg(r):
    r.sendline('/RESTORE private')
    private = r.recvrepeat(timeout=1).decode()
    r.sendline('/RESTORE public')
    public = r.recvrepeat(timeout=1).decode()
    print(private + '\n' + public)
    return r

register_user(r)
users = list_users(r)
login_user(r,username,password)
send_msg(r,'flag','kf8msb890lxw') #service corrupt !
restore_msg(r) #service corrupt !
r.close()


