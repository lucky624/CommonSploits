#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, re, requests
from storage import storage_set, storage_get
import string, random, uuid, re

ip = '10.218.1.3'


s = requests.Session()

html = s.post('https://{}:2300/crypto'.format(ip),timeout=(None,None),data={'message':'hi','text':'hi','client_password':'123qwe'},verify=False)
print(html.text)