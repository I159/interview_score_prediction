import json

from bottle import request, response, route, get, run, default_app

from data_set_preprocessor import data_set_preprocessor


app = application = default_app()


@route('/candidate/hired', method=['POST'])
def is_hired():
    data_set_preprocessor.parse_data_set()
    response.content_type = 'application/json'
    return json.dumps({"hired": True})

def main():
    run(host='localhost', port=8080)
