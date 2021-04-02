import os
import json
import sys
import json
import subprocess
import re
import urllib.request
import urllib.parse



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
    DEF = '\033[97m'

argz = sys.argv[1]
login = False
dirname = os.path.dirname(__file__)

# def run(string):
  
#     regex = re.compile('[@]')
#     if(regex.search(string) == None):
#         print("TODO check username col in DB for user")
          
#     else:
#         print("TODO check email for user login")


# if(login == False):
#         ok = input("Please input your email or username\n")
#         print(ok)
#         run(ok)



try:
        url = f"https://radroute.run/files/{argz}"
        req = urllib.request.urlopen(url)
        encoding = req.read().decode('utf-8')
        data = json.loads(encoding)
        ext = data[0]['ext']
        evalStatement = data[0]['pFile']
except:
        print(f'{co.FAIL} Please check your API call {co.DEF}')raise
        sys.exit(1)
try:
#run py program in masterRunner
        if ext == 'py':
                # print(data[0]['pFile'])
                bro = compile(evalStatement, 'evalCompile', 'exec')
                exec(bro)
        #print txt to console
        if ext == 'txt':
                print(data[0]['pFile'])
                
        #Eval to noder for JS runner
        if ext == 'js':
                
                os.system(f"node {dirname}/noder.js {argz}")

        if ext == 'rb':
                os.system(f"ruby {dirname}/rubyRunner.rb {argz}")

        # if ext == 'java':
        #         print(argz)
        #         x = data[0]['pFile']
        #         xSan = json_util.dumps(x)
        #         os.system(f"java JavaRunner {xSan}")
except KeyboardInterrupt:
        print(f"{co.WARN}Shutting down {argz} {co.DEF}")
except:
        print(f'{co.FAIL} Something something it was the other langs fault...Python out (╯°□°)╯︵ ┻━┻ {co.DEF}')
        sys.exit(1)
        # raise