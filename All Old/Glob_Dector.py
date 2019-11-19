# This File Is Genrated By A Naynesh Rathod
# Welcome to Naynesh Rathod PYTHON Prpgrams
import glob
import os

while True:
    ch = int(input("Enter Your Choice \n"+
                   "1 for Main Directory\n" +
                   "2 For Sub directory\n" +
                   "3 For See Only text File\n" +
                   "4 For See Start Form Item \n"))

    if ch <= 5:
        dir_name = input("Enter Directory Name ")
        os.chdir(dir_name)
        if ch == 1:
            fn = os.getcwd() + "/*"
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

            fn = os.getcwd() + "/+sample*.txt"
            for name in glob.glob(fn):
                print(name)
        if ch == 5:
            fn = os.getcwd() + "/*[0-9]*"
            for name in glob.glob(fn):
                print(name)
    else:
        exit()
