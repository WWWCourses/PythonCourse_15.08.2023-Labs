import requests


URL = 'http://127.0.0.1:5050'

def test_GET():
    r = requests.get(URL)

    print(f'RESPONSE: ')
    print(r.headers)

    if r.ok:
        print(r.text)


def test_POST():
    user_name= 'Pesho'

    r = requests.post(URL, data={'user_name':user_name})

    if r.ok:
        print(r.text)


test_POST()