import os
from flask_restful import Resource, Api

class Home(Resource):
    
    def get(self):
        os.system(f"cd ..")
        os.system(f"bash Bashrunner.sh")

        return {'hello': 'world'}