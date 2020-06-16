#!/usr/bin/env python

import redis
import sys


IP = '192.168.0.100'
#IP = sys.argv[1]
PORT = 6379

PASSWORD = ''
DATABASE = 0
PREFIX = ''

redis = redis.Redis(host=IP,
                    port=PORT,
                    password=PASSWORD,
                    db=DATABASE,
                    socket_timeout=None,
                    ssl_ca_certs='/home/dev/PycharmProjects/CommonExploits/db_dumpers/ca-certificate.crt')



for key in redis.scan_iter(match=f'{PREFIX}*'):
    print(key, flush=True)
    key_type = redis.type(key)
    try:
        if key_type == b'string':
            result = redis.get(key)
        elif key_type == b'set':
            result = redis.smembers(key)
        elif key_type == b'hash':
            result = redis.hgetall(key)
        elif key_type == b'list':
            result = redis.lrange(key, 0, -1)
        elif key_type == b'zset':
            result = redis.zrange(key, 0, -1)
        else:
            result = redis.get(key)
        print(result, flush=True)
    except:
        continue
