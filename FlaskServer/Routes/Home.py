import os
from flask_restful import Resource, Api

class Home(Resource):
    
    def get(self):
     
     

        return {'hello': 'world'}