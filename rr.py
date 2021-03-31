#!/usr/bin/env python3

import sys
import os
import subprocess
import json
 
 
argz = sys.argv

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
operating_system = sys.platform

req_installed=False
pymong_installed=False

def checkInstalled(r,p):
    pip_installs = subprocess.check_output(["pipenv", "run", "pip", "list", "--format", "json"])
    results = json.loads(pip_installs)

    for x in results:
        if(x['name']=='requests'):
            r=True
            print('req installed')
            # pass
        if(x['name']=='pymongo'):
            p=True
            print('pymonog installed')
            # pass
    # print(operating_system)

    if(r!=True):
        os.system('pipenv install requests')
    if(p!=True):
        os.system('pipenv install pymongo')



def doThing(command, *args, **kwargs):
    dirname = os.path.dirname(__file__)
    
    argList = []
    for arg in command:
        argList.append(arg)
    # print(argList)
    # binLoc= argList[0]
   
    if(args!=None):
        command = argList[1]
        if(command=='-v' or command=='-version' or command == '--v' or command=='--version'):
            print("=======================================================")
            print('\n too early for that; .000001 maybe \n')
            print("=======================================================")
            return 
        if(command=='-h' or command=='-help'):
            print("=======================================================")
            print("\n -v  or -version    ||  to see the version number")
            print("\n -h  or -help       ||  to see this help text")
            print("\n -r  or -run or run ||  to run a route directly from Rad Routes ")
            print(" route should follow -r. Command will look like example below;")
            print("               rr -r my-rad-route \n")
            print("=======================================================")
            return
        try:
            if(command=='-r'or command=='run' or command == '-run' or command == 'r'):
                if (len(argList)>=3):
                    route = argList[2]
                else:
                    print(f'{co.WARN}\n No Route Given, Please declare a route. to be ran after the -r \n \n see rr -h for help')
                    return
            # print(mod)
            if(operating_system=='win32'):
                os.system(f'pipenv run py {dirname}/runners/MasterRunner.py {route}')
                return
            else:
                os.system(f'pipenv run python3 ~/.rad_routes/rad-route-runner-master/runners/MasterRunner.py {route}')
                return
        except:
            print(f'{co.FAIL} Improper route or run command, please see $:"rr -h" for help.')
            raise
        if(command=='-u'or command=='upload' or command == '-upload' or command == 'up' or command == '-up' or command == 'uplad'):
            route = argList[2]
            return
        else:
            print(f"{co.WARN}\n \n Was not a known Rad Routes command;\n \n Run $: rr -h for help with commands")
try:
    checkInstalled(req_installed,pymong_installed)
    doThing(argz)
except KeyboardInterrupt:
    print(f'Shutting down {argz} and R.A.D. Runner byeeeeeeeeeeeeeeeeeeeee.')
    sys.exit()
except:
#   print( str(argz[2]) + " Was not a proper Rad Route command;\n \nCheck rr -h for help with commands")
  print(f"{co.FAIL}  Was not a proper Rad Route command;\n \nCheck rr -h for help with commands")
  raise
