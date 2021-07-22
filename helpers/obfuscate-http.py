import requests
import string, random, uuid
from evil_gen import generate_payload

def flag_generator(size=31, chars=string.digits + string.ascii_uppercase): # фэйковые флаги [A-Z0-9]{31}=
    return ''.join(random.choice(chars) for _ in range(size)) + '='

def header_generator(size=10, chars= string.ascii_uppercase):  # фэйковые хэдеры
    return ''.join(random.choice(chars) for _ in range(size))

non_standart_http_headers = {
    'Save-Data' : 'on',
    'X-Request-ID' : 'f058ebd6-02f7-4d3f-942e-904344e8cde5',
    'X-Csrf-Token' : 'i8XNjC4b8KVok4uw5RftR38Wgp2BFwql',
    'Proxy-Connection' : 'keep-alive',
    'x-wap-profile' : 'http://wap.samsungmobile.com/uaprof/SGH-I777.xml',
    'X-Att-Deviceid' : 'GT-P7320/P7320XXLPG',
    'X-HTTP-Method-Override' : 'DELETE',
    'Front-End-Https' : 'on',
    'X-Forwarded-Proto' : 'https',
    'X-Forwarded-Host' : 'en.wikipedia.org',
    'DNT' : '1',
    'X-UIDH' : 'swag'
}

flag_headers = {
header_generator() : flag_generator(), # создаём фэйковые хэдеры с флагами
}

users = ['alex', 'lucky', 'pseudo_eva', 'arkiix']
for user in users:
    s = requests.Session()   # для атаки по юзерам - для каждого используем новую сессию
    s.get(user)

generate_payload()  # вернёт рандомный фэйк пэйлоад

