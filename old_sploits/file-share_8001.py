#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, re, requests
import string, random, uuid

def generator(size=12, chars= string.ascii_lowercase ):
    return ''.join(random.choice(chars) for _ in range(size))

def generator_pass(size=22, chars=string.digits + string.ascii_uppercase + string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))

#ip = sys.argv[1]
ip = '10.1.59.1' + ':8001'
url = 'http://{}'.format(ip)

s = requests.Session()

print(generator_pass() + '$')

html = s.get(url + '/Identity/Account/Register?returnUrl=/authentication/login', timeout=(None,None)).text
cookies = s.cookies.get_dict()
for item in cookies:
    name = item
    value = cookies[item]


token = re.search('<input name="__RequestVerificationToken" type="hidden" value="(.*)" /></form>', html).group(1)

email = generator() + '@test.de'
password = generator_pass() + '$'

data = 'Input.Email={}&Input.Password={}&Input.ConfirmPassword={}&__RequestVerificationToken={}'.format(email, password,password, token)

data = {
        'Input.Email': email,
        'Input.Password': password,
        'Input.ConfirmPassword': password,
        '__RequestVerificationToken': token,
}



headers = {'Content-Type' : 'application/x-www-form-urlencoded'}

html =s.post(url + '/Identity/Account/Register?returnUrl=/authentication/login',data=data, headers=headers, timeout=(None,None))


print(html.history)

for resp in html.history:
    print(resp.status_code, resp.url)
