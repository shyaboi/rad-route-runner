import os
import json
import requests

response = requests.get("http://localhost:5000/files/bro")

data = response.json()
evalStatement = data[0]['pFile']
ext = data[0]['ext']

if ext == 'py':
        print(data[0]['pFile'])
        bro = compile(evalStatement, 'bra', 'exec')
        exec(bro)
# ok = json.loads(data)
