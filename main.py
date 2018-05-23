import json

from bottle import request, response, route, get, run, default_app


app = application = default_app()


@route('/candidate/<application_id>', method=['POST'])
def update_delete_handler(application_id):
    response.content_type = 'application/json'
    return json.dumps({"hired": True})

def main():
    run(host='localhost', port=8080)
