#!/usr/bin/env python

import sys
import os
argz = sys.argv


def doThing(command, *args, **kwargs):

    argList = []
    for arg in command:
        argList.append(arg)
    # print(argList)
    # binLoc= argList[0]
   
    if(args!=None):
        command = argList[1]
        if(command=='-v'):
            print("=======================================================")
            print('\n too early for that; .000001 maybe \n')
            print("=======================================================")
            return 
        if(command=='-h'):
            print("=======================================================")
            print("\n -v  or -version    ||  to see the version number")
            print("\n -h  or -help       ||  to see this help text")
            print("\n -r  or -run or run ||  to run a route directly from Rad Routes \n")
            print("=======================================================")
            return
        if(command=='-r'):
            mod = argList[2]
            # print(mod)
            os.system(f'py MasterRunner.py {mod}')
            return
        else:
            print('\n'+str(command) + "\n \n Was not a proper command;\n \nCheck rr -h for help with commands")
        
try:
    doThing(argz)
except:
  print(str(argz) + " Was not a proper command;\n \nCheck rr -h for help with commands")
