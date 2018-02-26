from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from csv2json import convert, load_csv, save_json
import json


app = Flask(__name__)
api = Api(app)

reg_totals = json.load(open('totals.json', 'r'))


class ReturnObject(Resource):
    def get(self):
        return reg_totals


api.add_resource(ReturnObject, '/')


if __name__ == '__main__':
    app.run(debug=True)
