import redis


IP = '127.0.0.1'
PORT = 6379

PASSWORD = ''
DATABASE = 0
PREFIX = ''

redis = redis.Redis(host=IP,
                    port=PORT,
                    password=PASSWORD,
                    db=DATABASE,
                    socket_timeout=None)

def storage_set(value,flag='lol'):
    try:
        redis.set(value, flag)
    except:
        print('storage error')
    return value

def storage_get(value):
    try:
        if redis.exists(value):
            return True
        else:
            return False
    except:
        print('storage error')
        return False