import os
import json
import requests
import sys
argz = sys.argv[1]

response = requests.get(f"http://localhost:5000/files/{argz}")
data = response.json()
evalStatement = data[0]['pFile']
ext = data[0]['ext']

if ext == 'py':
        print(data[0]['pFile'])
        bro = compile(evalStatement, 'evalCompile', 'exec')
        exec(bro)
if ext == 'txt':
        print(data[0]['pFile'])
if ext == 'js':
        pd = data[0]['pFile']
        os.system(f"node noder.js {data}")

# ok = json.loads(data)
