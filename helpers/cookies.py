#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, re, requests, requests.cookies

#ip = sys.argv[1]
ip = '192.168.0.104'
jar = requests.cookies.RequestsCookieJar()

#Show cookies in Google Chrome
#Ctrl + Shift + J >> Application

with requests.Session() as s:
    one = requests.cookies.RequestsCookieJar()
    two = requests.cookies.RequestsCookieJar()
    three = requests.cookies.RequestsCookieJar()

    one.set('PHPSESSID','21cf470862e9fbd08fa261c49af4065d')
    two.set('security_level','0')
    three.set('top_security','no')

    one.update(two)
    one.update(three)
    s.cookies = one

    html = s.get('http://{}/bWAPP/portal.php'.format(ip))

    print(html.text)

