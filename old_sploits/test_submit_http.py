import requests,json

headers = {
    'X-Team-Token': 'your_secret_token',
}


flags = ['0000000000000000000000000000001=','0000000000000000000000000000002=']


answer = requests.put('http://localhost/flagsubmit', json=flags, headers=headers)

print(answer.text)



