#!/usr/bin/env python

import sys
argList = []

for arg in sys.argv:
    argList.append(arg)

binLoc= argList[0]
mod = argList[1]
def comm(cmd='Default'):
    if(argList[2]):
        res = argList[2]
        return res
    else:
        print('noargs')

if(mod=='-h' or '-help'):
    print(" -v  or -version    ||  to see the version number")
    print(" -h  or -help       ||  to see this help text")
    print(" -r  or -run or run ||  to run a route directly from Rad Routes")
    print("Working on more...")
elif(mod=='--v'or'--version'):
    print('too early for that; .000001 maybe')
elif(mod=='--v'or'--'):
    print('')