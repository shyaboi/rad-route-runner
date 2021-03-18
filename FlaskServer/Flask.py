from flask import Flask
from flask_restful import Resource, Api
import os 
from Routes import Home, SaveFile, GetFile, Exists, AceFile, AllRoutes
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

api = Api(app)

api.add_resource(Home, '/')

api.add_resource(SaveFile, '/file')

api.add_resource(AceFile, '/aceFile')

api.add_resource(AllRoutes, '/all')

api.add_resource(GetFile, '/files/<string:route>')

api.add_resource(Exists, '/exists/<string:route>')



if __name__ == '__main__':
    app.run(debug=True)