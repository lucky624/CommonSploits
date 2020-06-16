import string, random, uuid

#hex digits
def generator(size=20, chars=string.digits):
    return hex(int(''.join(random.choice(chars) for _ in range(size))))
print(generator()[2:])

#uuid
print(str(uuid.uuid4()))

#hex_uuid
print(uuid.uuid4().hex)

#flags [A-Z0-9]{31}=
def generator(size=31, chars=string.digits + string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size)) + '='
print(generator())

#users
def generator(size=12, chars=string.digits + string.ascii_letters):
    return ''.join(random.choice(chars) for _ in range(size))
print(generator())

