import os
import shutil


def mvp(path, vr):
    if vr == 0:
        return path
    else:
        return path + "" + str(vr)


def rotate(path, vr=0):
    olpath = mvp(path, vr)
    if not os.path.exists(olpath):
        raise IOError("'%'doesn't exist" % path)
    n_path = mvp(path, vr + 1)
    if os.path.exists(n_path):
        rotate(path, vr + 1)
    shutil.move(olpath, n_path)


def rotate_log_file(path):
    file = "C:\\Users\\Naynesh"
    if not os.path.exists(path):
        nfile = open(path, "w")
        del nfile
    print(rotate(path))


rotate_log_file("naynesh.log")
