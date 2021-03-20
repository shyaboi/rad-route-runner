import os
import json
import requests
import sys
from flask_restful import Resource, Api, reqparse
import json
from bson import json_util
import subprocess
class co:
    HEADER = '\033[95m'
    OKBL = '\033[94m'
    OKCY = '\033[96m'
    OKGR = '\033[92m'
    WARN = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
argz = sys.argv[1]


try:
        response = requests.get(f"http://localhost:5000/files/{argz}")
        data = response.json()
        ext = data[0]['ext']
        evalStatement = data[0]['pFile']
except:
        raise TypeError(f'{co.FAIL} Please check your API call')
try:
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
except:
        print('something something it was the other langs fault...Python out (╯°□°)╯︵ ┻━┻')
        raise