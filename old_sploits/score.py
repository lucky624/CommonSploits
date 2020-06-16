import requests, json,re

html = requests.get('https://cbsctf.live//api/teams/').text

for item in json.loads(html):
    print('\'' + item['name'] + '\':\'' + item['ip'] + '\',')
