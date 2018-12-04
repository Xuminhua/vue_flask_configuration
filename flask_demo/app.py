#!/usr/bin/python3
# coding: utf-8
import json

from flask import Flask
from flask import make_response, jsonify

app = Flask(__name__)


def get_json():
    a = {"answer": "yes", "forced": False}

    response = make_response(jsonify(a))

    # response = make_response(json.dumps(a))
    # response.headers['Access-Control-Allow-Origin'] = '*'
    # response.headers['Access-Control-Allow-Methods'] = 'POST'
    # response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return response


@app.route('/')
def hello_world():
    return get_json()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
