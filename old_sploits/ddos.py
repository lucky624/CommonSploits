#!/usr/bin/env python3
import requests



while(True):
    try:
        requests.get('http://161.35.18.165:9090', timeout=(0.125,0.125))
    except requests.exceptions.ConnectTimeout:
        continue