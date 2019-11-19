#
import os
print("Your working on current this file:\n"+os.getcwd()) #Read a path
print("\n In that folder all file are:")
a=os.listdir()
for i in a:
    print("\n",i)