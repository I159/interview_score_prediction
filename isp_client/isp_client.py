import requests


def main():
    r = requests.post(
        'http://localhost:8080/candidate/hired',
        data={
            'key': 'value'})
    print(r.json())
