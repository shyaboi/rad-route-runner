import os
from flask_restful import Resource, Api
from flask_restful import reqparse
from flask import  request

class File(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('type')
        args = parser.parse_args()

        f = request.files['file']

        # fileExt = str(f).split(".")[-1]
        fileExt = args.type
        print(f)

        if fileExt == "python":
            print("doing py things")
        if fileExt == "ruby":
            print("sinhy")
        # print(fileExt)
        return "thanks bud"