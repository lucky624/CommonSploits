#!/usr/bin/env python3
import string, random, uuid
from socket import *
import sys,string,random,re
import codecs

def generator(size=32, chars=string.digits + string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size)) + '='

def generator_int(size=10, chars=string.digits):
    return hex(int(''.join(random.choice(chars) for _ in range(size))))

IP = "192.168.0.102"
port = 8888
TIMEOUT = 0.5
def readall(s):
    mes=b''
    try:
        while 1:
            m = s.recv(1)
            mes += m
    except timeout:
        return mes.decode()

def put(flag_id, flag):
    FLAG_ID = flag_id
    FLAG = flag
    #putting flag
    s = socket(AF_INET, SOCK_STREAM)
    s.settimeout(TIMEOUT)
    s.connect((IP, port))
    mes = readall(s)
    if not (u'1. Подойти к лавке со свечками.' in mes and u'2. Подойти к священнику.' in mes and u'3. Прочитать молитву.' in mes):
        exit(103)
    s.send(b'2\n')
    mes = readall(s)
    if not (u'1. Исповедаться.' in mes and u'2. Я хочу повысить свой ' in mes and u'3. Уйти.' in mes):
        exit(103)
    s.send(b'1\n')
    mes = readall(s)
    if (not u'Как вас зовут?' in mes):
        exit(102)
    s.send((FLAG_ID + '\n').encode())
    mes = readall(s)
    if not(u'Хочешь что-то добавить') or not(u'всегда можешь высказаться'):
        exit(102)
    s.send((FLAG + '\n').encode())
    mes = readall(s)
    if not(u'Вы исповедались.' in mes):
        exit(102)
    print('Put OK')
    #print(FLAG_ID)
    s.close()

while True:
    put(generator_int(), generator())

