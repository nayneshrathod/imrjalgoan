import os

fname = input("Enter the File Name")
dirpath = input("Enter the Path")
os.chdir(dirpath)
fullpath = os.path.join(dirpath, fname)

if os.path.exists(fullpath):
    f = open(fname, "a")
    msg = input("Enter the Content")
    f.write(msg)
    f.close()

else:
    f = open(fname, "x")
    msg = input("Enter the Content")
    f.write(msg)
    f.close()
