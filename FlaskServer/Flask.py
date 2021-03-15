from flask import Flask
from flask_restful import Resource, Api
import os 
from Routes import Home,File


app = Flask(__name__)

api = Api(app)

api.add_resource(Home, '/')

api.add_resource(File, '/file')

if __name__ == '__main__':
    app.run(debug=True)