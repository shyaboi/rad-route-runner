import os
import json
import requests
import sys
from flask_restful import Resource, Api, reqparse
import json
from bson import json_util
import subprocess

argz = sys.argv[1]

response = requests.get(f"http://localhost:5000/files/{argz}")
data = response.json()
evalStatement = data[0]['pFile']
ext = data[0]['ext']
 
#run py program in masterRunner
if ext == 'py':
        print(data[0]['pFile'])
        bro = compile(evalStatement, 'evalCompile', 'exec')
        exec(bro)
#print txt to console
if ext == 'txt':
        print(data[0]['pFile'])
#Eval to noder for JS runner
if ext == 'js':
        x = data
        xSan = json.loads(json_util.dumps(x))
        os.system(f"node noder.js {data}")

if ext == 'rb':
        os.system(f"ruby rubyRunner.rb {argz}")

if ext == 'java':
        print(argz)
        x = data[0]['pFile']
        xSan = json_util.dumps(x)
        os.system(f"java JavaRunner {xSan}")
