#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os,re
import string, random, uuid
os.environ['PWNLIB_NOTERM'] = 'True'
from pwn import *

#ip = sys.argv[1]
ip = '192.168.0.100'
port = 8080

r = remote(ip, port)

def generator(size=12, chars=string.digits + string.ascii_letters):
    return ''.join(random.choice(chars) for _ in range(size))

login = 'rrr'
password = 'rrr'

def login_user(r,login,password,logged=False):
    r.recvuntil('You login:')
    r.sendline(login)
    r.recvuntil('You pass:')
    r.sendline(password)
    r.recvrepeat(timeout=0.5)
    if not logged:
        r.recvuntil('\nWhat is your role? Writer (w), reader (r):\n')
    return r

def menu_writer(r):
    r.sendline('w')
    r.recvuntil('3)Viwe your task\n')
    return r

def writer_1_put_task(r,task_text,phrase):
    r.sendline('1')
    r.recvuntil('Enter task text:\n')
    r.sendline(task_text)
    r.sendline()
    r.recvuntil('What do you want to say to the person who decides this task?\n')
    r.sendline(phrase)
    r.recvuntil('Press ctrl+c for exit\n')
    return r

def writer_2_put_test(r,task_number,input_data,output_data):
    r.sendline('2')
    r.recvuntil('Enter task number:\n')
    r.sendline(task_number)
    r.recvuntil('Input data:\n')
    r.sendline(input_data)
    r.recvuntil('Output data:\n')
    r.sendline(output_data)
    r.recvuntil('Press ctrl+c for exit')
    return r

def writer_3_view_task(r,task_number):
    r.sendline('3')
    r.recvuntil('Enter task number:\n')
    r.sendline(task_number)
    r.recvuntil('Press ctrl+c for exit')
    return r

def menu_reader(r):
    r.sendline('r')
    r.recvuntil('2)Pass task.\n')
    return r

def reader_1_get_task(r):
    r.sendline('1')
    task_numbers = r.recvrepeat(timeout=1).decode()
    task_numbers = re.search('Available tasks for you:\n(.*)\nEnter task number', task_numbers, re.S).group(1)
    task_numbers.split(' ')
    r.sendline(task_numbers[0])
    print(r.recvrepeat(timeout=1).decode())
    return r

def reader_2_pass_task(r,task_number):
    r.send('2\n'.encode())
    r.recvuntil('Enter task number\n')
    r.sendline(task_number)
    r.recvuntil('Paste your code:\n')
    r.sendline('int main(void){return 0;}')
    r.send('\n'.encode())
    print(r.recvrepeat(timeout=0.5))
    return r


login_user(r,login,password,logged=True)
#menu_reader(r)

reader_2_pass_task(r,'1')

r.close()


