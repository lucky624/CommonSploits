#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, re, requests, requests.cookies
import string, random, uuid, re

#ip = sys.argv[1]
ip = '192.168.0.100'

s = requests.Session()

def generator(size=8, chars=string.digits + string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))

jar = requests.cookies.RequestsCookieJar()

proxies = {
  'http': 'http://127.0.0.1:8080',
  'https': 'http://127.0.0.1:8080',
}

username = generator()
password = username
mail = username + '@mail.ru'

print(username)
print(password)
print(mail)


def register_user(s):
    auth = {
        'register' : 'True',
        'inputLogin': username,
        'inputEmail': mail,
        'inputPublicName': username,
        'inputPassword1': password,
        'inputPassword2': password,
        'form':'sumbit'
    }
    #files = {'picture': open('image.png', 'rb')}
    files = {'picture': ('image.png', open('image.png', 'rb'), 'image/png')}
    html = s.post('http://{}/registration.php'.format(ip),files=files, data=auth)
    return s

def login_user(s):
    s.post('http://{}/login.php'.format(ip),data={'inputEmailorLogin': username,'inputPassword': password,'signin':''})
    html = s.get('http://{}/user_info.php'.format(ip))
    #print(html.text)
    return s

def get_threads(s):
    threads = []
    html = s.get('http://{}/threads.php?section=anime'.format(ip))
    print(re.findall('<p>(.*)</p>', html.text))
    id_anime = re.findall('<a class="btn btn-outline-primary btn-sm" href="\/thread.php\?id=(\d)">Ответить<\/a>',html.text)
    html = s.get('http://{}/threads.php?section=cosplay'.format(ip))
    print(re.findall('<p>(.*)</p>', html.text))
    id_cospley = re.findall('<a class="btn btn-outline-primary btn-sm" href="\/thread.php\?id=(\d)">Ответить<\/a>',html.text)
    html = s.get('http://{}/threads.php?section=manga'.format(ip))
    print(re.findall('<p>(.*)</p>', html.text))
    id_manga = re.findall('<a class="btn btn-outline-primary btn-sm" href="\/thread.php\?id=(\d)">Ответить<\/a>',html.text)
    for thread in id_anime:
        threads.append(thread)

    for thread in id_cospley:
        threads.append(thread)

    for thread in id_manga:
        threads.append(thread)

    return

def create_thread(s,theme,msg):
    data = {
        'theme' : theme,
        'message' : msg,
        'save': 'True'
    }
    files = {'picture': ('image.png', open('image.png', 'rb'), 'image/png')}

    html = s.post('http://{}/threads.php?section=anime'.format(ip),files=files,data=data)

    return s

def answer_by_thread(s,id):
    data = {
        'theme': 'theme_kek',
        'message': 'msg',
        'save': 'True'
    }
    files = {'picture': ('image.png', open('image.png', 'rb'), 'image/png')}
    html = s.post('http://{}/thread.php?id={}'.format(ip,id), files=files, data=data)
    #print(html.text)
    return s


register_user(s)
login_user(s)
get_threads(s)
create_thread(s,'theme','msg')
answer_by_thread(s,'1')
