import os
from flask_restful import Resource, Api
from flask_restful import reqparse

class File(Resource):
    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('file')
        args = parser.parse_args()
        
        return args