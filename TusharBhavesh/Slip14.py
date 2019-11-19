import os
fname=input("Enter the File Name")
path=input("Enter the PAth")
#fullpath=os.path.join(path,fname)
os.chdir(path)
co=0
try:
    f=open(fname,"r")
    f1=f.readlines()
    print("Total No. of Lines",len(f1))
    for item in f1:
        cnt=item.split()
        co+=len(cnt)
        for i in item.split('.'):
            print(i)
    print("Total number of words",co)
except IOError:
    print("File Does Not Exist")

finally:
    f.close()
