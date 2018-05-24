"""
Infrastructure interface.

Strict data transfer module.
"""
import json

from bottle import request, response, route, get, run, default_app

from data_application import data_app

app = application = default_app()


@route('/candidate/hired', method=['POST'])
def is_hired():
    hired = data_app.predict()
    response.content_type = 'application/json'
    return json.dumps({"hired": hired})

def main():
    run(host='localhost', port=8080)
