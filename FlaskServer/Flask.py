from flask import Flask
from flask_restful import Resource, Api
import os 
# import requests


# url = 'https://uselessapi.com/u-c-r/test'
# url = 'https://uselessapi.com/u-c-r/rick'
# url = 'https://uselessapi.com/u-c-r/toast'

# print("Py rrGetter running!")

# x = requests.get(url)

# ae = x.headers

# ct = ae.get('Content-Type')

# dk= str(x.content)

# cl= dk.replace("b'",'',1)
# fcl= cl.replace("'",'',1)


# if ct=="text/html; charset=utf-8":
#     print('html or txt')
#     os.system(f"python -m webbrowser -t {url}")
#     pass

# if ct=="application/json; charset=utf-8":
#     print('json')
#     pass

# if d[0]=="<":
#     pass
# print("fin")

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