from flask import Flask
from flask_restful import Resource, Api
import os 
from Routes import Home,SaveFile,GetFile


app = Flask(__name__)

api = Api(app)

api.add_resource(Home, '/')

api.add_resource(SaveFile, '/file')

api.add_resource(GetFile, '/files/<string:route>')

if __name__ == '__main__':
    app.run(debug=True)