import json

from bottle import request, response, route, get, run, default_app

from data_set_preprocessor import data_set_preprocessor
from model_builder import model_builder


app = application = default_app()


@route('/candidate/hired', method=['POST'])
def is_hired():
    data_set = data_set_preprocessor.parse_data_set()
    model_builder.learn(data_set)
    response.content_type = 'application/json'
    return json.dumps({"hired": True})

def main():
    run(host='localhost', port=8080)
