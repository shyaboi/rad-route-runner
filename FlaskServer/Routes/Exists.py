from DBConn import mongo
from flask_restful import Resource, Api
from bson import json_util, ObjectId
from flask_restful import Resource, Api, reqparse
import json
from bson import json_util


class Exists(Resource):

    def get(self,route):
        t=True
        f=False
        res='unassign';
        parser = reqparse.RequestParser()
        rr = parser.add_argument('route',route)
        args = parser.parse_args()
        rr = str(args.route)

        k =  mongo.db.radRoute.find_one({ 'route':route}, { "$exists: true", "$ne: null" })

        if k==None:
            res = f
        if k != None:
            res = t

        return res