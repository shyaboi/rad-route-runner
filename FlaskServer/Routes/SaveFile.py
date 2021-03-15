import os
from flask_restful import Resource, Api, reqparse
from flask import  request
import shutil 
from DBConn import mongo

class SaveFile(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('type')
        parser.add_argument('route')
        args = parser.parse_args()
        f = request.files['file']

        parsedFile = f.read().decode('utf-8')
        fileExt = args.type
        route = args.route
        mongo.db.radRoute.insert({'route':route, 'ext':fileExt, 'pFile':parsedFile, 'fileKey':route+f.filename})
        # ff = f.save(f.filename)
        # shutil.move(f.filename, f"./uploads/{f.filename}")
        mongo.save_file(route+f.filename, f)

        return "COol"