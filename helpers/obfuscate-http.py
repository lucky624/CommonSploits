import requests, requests.cookies
import string, random, uuid
from evil_gen import generate_payload
from time import sleep

def flag_generator(size=31, chars=string.digits + string.ascii_uppercase): # фэйковые флаги [A-Z0-9]{31}=
    return ''.join(random.choice(chars) for _ in range(size)) + '='

def header_generator(size=10, chars= string.ascii_uppercase):  # фэйковые хэдеры
    return ''.join(random.choice(chars) for _ in range(size))

non_standart_http_headers = {  # нестандартные хэдеры
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

generate_payload()  # вернёт рандомный фэйк пэйлоад

users = ['alex', 'lucky', 'pseudo_eva', 'arkiix']  # get user list
for user in users:
    s = requests.Session()      # получаем и сохраняем сессию в редиску
    auth = {
        'username' : 'lucky624',
        'password': 'lucky624'
    }
    s.post('url' , json=auth)

    # здесь поток фэйковых данных (пэйлоады, кастомовые хэдеры, странные действия) - обязательно с первой сессией

    w = requests.Session() # новая сессия с тру пэйлоадамом в перемешку с фэйковыми
    sleep(random.randint(5,20))  # делаем рандомный слип между запросами
    w.get(user)

    # здесь поток фэйковых данных (пэйлоады, кастомовые хэдеры, странные действия) - обязательно со второй сессией




