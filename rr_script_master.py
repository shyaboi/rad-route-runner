#!/usr/bin/env python

import sys
import os
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

def doThing(command, *args, **kwargs):

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
                os.system(f'cd ./runners && py MasterRunner.py {route}')
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
    doThing(argz)
except:
#   print( str(argz[2]) + " Was not a proper Rad Route command;\n \nCheck rr -h for help with commands")
  print(f"{co.FAIL}  Was not a proper Rad Route command;\n \nCheck rr -h for help with commands")
  raise
