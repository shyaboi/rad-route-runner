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
    DEF = '\033[97m'
operating_system = sys.platform

pymong_installed=False

def checkENV():
#TODO check for env environment, check for install...if no install, install, if no env on, but installed, start env...give user flag to choose different env and change env executeing command
    try:
        if(os.environ['VIRTUAL_ENV']):
            print(os.environ['VIRTUAL_ENV'])
    except KeyError:
        print('no env')





def doThing(command, *args, **kwargs):
    dirname = os.path.dirname(__file__)
    
    argList = []
    for arg in command:
        argList.append(arg)
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
                    if (len(argList)>=4):
                        arg_mods = []
                        al = len(argList)
                        for x in range(3, al):
                            i = argList[x]
                            arg_mods.append(i)
                        rest = arg_mods
                        if('-v' in rest or 'env' in rest):
                            print(f'{co.WARN}\n R.A.D. Routes virtual environment runner is experimental and may not function properly...YOLO!!!!!! {co.DEF}')
                            checkENV()
                            os.system(f" echo Running {route} in SPECIFIED virtual python environment")
                            if(operating_system=='win32'):
                                os.system(f'pipenv run py {dirname}/runners/MasterRunner.py {route}')
                                return
                            else:
                                os.system(f'pipenv run python3 ~/.rad_routes/rad-route-runner-master/runners/MasterRunner.py {route}')
                            return

                    else:
                        pass
                else:
                    print(f'{co.WARN}\n No Route Given, Please declare a route. to be ran after the -r \n \n see rr -h for help {co.DEF}')
                    return
            # print(mod)
            if(operating_system=='win32'):
                os.system(f'py {dirname}/runners/MasterRunner.py {route}')
                return
            else:
                os.system(f'python3 ~/.rad_routes/rad-route-runner-master/runners/MasterRunner.py {route}')
                return
            if(command=='-u'or command=='upload' or command == '-upload' or command == 'up' or command == '-up' or command == 'uplad'):
                route = argList[2]
                return 'Updates from CLI coming soon!'
            if(command=='-u'or command=='upload' or command == '-upload' or command == 'up' or command == '-up' or command == 'uplad'):
                route = argList[2]
                return 'Updates from CLI coming soon!'
        except KeyboardInterrupt:
            print(f'{co.OKCY}Shutting down R.A.D. Runner byeeeeeeeeeeeeeeeeeeeee.{co.DEF}')
        except:
            print(f"{co.WARN}\n \n Was not a known Rad Routes command;\n \n Run $: rr -h for help with commands {co.DEF}")
        
try:
    doThing(argz)
except KeyboardInterrupt:
    sys.exit(1)  
except:
  print(f"{co.FAIL} \nWas not a proper Rad Route command;\n \nCheck rr -h for help with commands {co.DEF}")
  sys.exit(1)
#   raise
