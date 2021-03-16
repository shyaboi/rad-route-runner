from DBConn import mongo
from flask_restful import Resource, Api, reqparse
from DBConn import mongo
import json
from bson import json_util



class GetFile(Resource):
    def get(self,route):

        parser = reqparse.RequestParser()
        ffname = parser.add_argument('route',route)


        args = parser.parse_args()
        x = mongo.db.radRoute.find({'route':route})
        xSan = json.loads(json_util.dumps(x))
        
        return xSan