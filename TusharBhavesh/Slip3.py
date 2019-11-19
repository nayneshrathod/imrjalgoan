import os
import glob
while 1:
    ch=int(input("Enter 1.For See Main Directory\n2.For See Sub Directory\n3.For See only text files\n4.For see File Start form Item\n5.For show Files which have Nubmering\n6Exit"))
    if ch <= 5:
        dirpath=input("Enter the Path")
        os.chdir(dirpath)
        if ch == 1:
            fn=os.getcwd()+"/*"
            for name in glob.glob(fn):
                print(name)

        if ch == 2:
            fn = os.getcwd() + "/*/*"
            for name in glob.glob(fn):
                print(name)

        if ch == 3:
            fn = os.getcwd() + "/*.txt"
            for name in glob.glob(fn):
                print(name)

        if ch == 4:
            fn = os.getcwd() + "/*Item?.txt"
            for name in glob.glob(fn):
                print(name)

        if ch == 5:
            fn = os.getcwd()+"/*[0-9]*"
            for name in glob.glob(fn):
                print(name)
    if ch == 6:
        exit()