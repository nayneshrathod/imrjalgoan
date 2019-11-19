# dir path and property
import os
import time

path = input("Enter The Full Path ")
path_list = []
if os.path.exists(path):
    for i in os.listdir(path):
        full_path = os.path.join(path, i)
        file_size = os.path.getsize(full_path)
        acs_time = time.ctime(os.path.getatime(full_path))
        cri_time = time.ctime(os.path.getmtime(full_path))
        mod_time = time.ctime(os.path.getmtime(full_path))
        print(full_path, "Create time: ", cri_time, "file Size ", file_size, "create time ", cri_time, "Modified Time ",
              mod_time)

else:
    print("path Does Not Exist")
