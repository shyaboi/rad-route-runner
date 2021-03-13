from flask import Flask
from flask_restful import Resource, Api
import os 


app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    
    def get(self):
        os.system(f"cd ..")
        os.system(f"bash Bashrunner.sh")
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)