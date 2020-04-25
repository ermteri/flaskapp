#!/usr/bin/env python3

from flask import Flask, Response

from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app)


@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return Response('What', status=501)


if __name__ == '__main__':
    app.run(debug=True)
