#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, re, requests
import string, random, uuid, re


def generator(size=12, chars=string.digits + string.ascii_letters):
    return ''.join(random.choice(chars) for _ in range(size))



#ip = sys.argv[1]
ip = '10.61.21.2' + ':3000'

s = requests.Session()

#html = s.get('http://{}/chats'.format(ip))
#data = html.json()

username = generator()
password = generator()
chat = generator()

register = {'username': username, 'firstName': username, 'lastName': username, 'password': password, 'biography': ""}
auth = {'username': username, 'password': password}

html = s.post('http://{}/register'.format(ip), data=register)
html = s.post('http://{}/login'.format(ip), data=auth)
#html = s.post('http://{}/createChat'.format(ip), data={'chatName': chat})
#chatid = html.json()['data']['chatId']
#print(chatid)
#html = s.post('http://{}/joinChat'.format(ip), data={"inviteLink": chatid, "chatId": chatid})

firstnames = []
lastnames = []

for i in range(1,100):
    payload = {"query": {"firstName": {"$nin": []}, "lastName": {"$nin": []}}}
    html = s.post('http://{}/searchUser'.format(ip), data=payload)
    print(html.json())

#for user in data['data']['chats']:
    #userids = user['usersIds']
    #print(user)
    #for id in userids:
        #html = s.get('http://{}/user'.format(ip), params={'userId': id})
        #print(html.json()['data'])
        #firstname = html.json()['data']['firstName']
        #lastname = html.json()['data']['lastName']
        #firstnames.append(firstname)
        #lastnames.append(lastname)
        #payload = {"query": {"firstName": {"$nin": firstnames}, "lastName": {"$nin": lastnames}}}
        #html = s.post('http://{}/searchUser'.format(ip), data=payload)
        #print(html.json(), flush=True)
        #break
    #print(firstnames)
    #payload = {"query":{"firstName":{"$nin":firstnames}, "lastName": {"$nin": lastnames}}}
    #payload = {"query": {"firstName": {"$nin": []}, "lastName": {"$nin": []}}}
    #html = s.post('http://{}/searchUser'.format(ip), data=payload)
    #print(html.json(),flush=True)
    #firstnames.clear()


