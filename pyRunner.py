import requests
import os

# url = 'https://uselessapi.com/u-c-r/test'
# url = 'https://uselessapi.com/u-c-r/rick'
url = 'https://uselessapi.com/u-c-r/toast'

print("Py rrGetter running!")

x = requests.get(url)

ae = x.headers

ct = ae.get('Content-Type')

dk= str(x.content)

cl= dk.replace("b'",'',1)
fcl= cl.replace("'",'',1)

f = open("testFile.txt", "a")
f.write("\nText Written From pyRunner!\n")
f.close()

#open and read the file after the appending:
f = open("demofile3.txt", "r")
print(f.read())

print(fcl)

if ct=="text/html; charset=utf-8":
    print('html or txt')
    os.system(f"python -m webbrowser -t {url}")
    pass

if ct=="application/json; charset=utf-8":
    print('json')
    pass

# if d[0]=="<":
#     pass
# print("fin")