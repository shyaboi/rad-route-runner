import os



f = open("testFile.txt", "a")
f.write("\nText Written From pyRunner!\n")
f.close()

f = open("testFile.txt", "r")
print(f.read())


