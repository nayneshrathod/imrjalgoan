import os

dir_path = input("Enter Path")
os.chdir(dir_path)
print(os.listdir(dir_path))
