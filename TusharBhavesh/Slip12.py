import os
import time
dirpath=input("Enter the Path")
os.chdir(dirpath)

for item in os.listdir(dirpath):
    fullpath=os.path.join(dirpath,item)
    mtime=time.ctime(os.path.getmtime(fullpath))
    size=os.path.getsize(fullpath)
    print(fullpath,mtime,str(size))