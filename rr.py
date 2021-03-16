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
            print('too early for that; .000001 maybe')
            return 
        if(command=='-h'):
            print(" -v  or -version    ||  to see the version number")
            print(" -h  or -help       ||  to see this help text")
            print(" -r  or -run or run ||  to run a route directly from Rad Routes")
            return
        if(command=='-r'):
            mod = argList[2]
            print(mod)
            return
        else:
            print('\n'+str(command) + "\n \n Was not a proper command;\n \nCheck rr -h for help with commands")
        
try:
    doThing(argz)
except:
  print(str(argz) + " Was not a proper command;\n \nCheck rr -h for help with commands")
