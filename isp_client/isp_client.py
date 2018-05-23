import requests


def main():
    r = requests.post('http://localhost:8080/candidate/hired', data = {'key':'value'})
    __import__('pdb').set_trace()
    print(r.json())
