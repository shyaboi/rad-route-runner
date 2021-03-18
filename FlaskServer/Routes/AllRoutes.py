from DBConn import mongo
from flask_restful import Resource, Api, reqparse
from DBConn import mongo
import json
from bson import json_util



class AllRoutes(Resource):
    def get(self):
        allR = []
        for x in mongo.db.radRoute.find():
            allR.append(x)
            print(x)
        jDump = json.loads(json_util.dumps(allR))
        return jDump
