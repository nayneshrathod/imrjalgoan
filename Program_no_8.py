'''
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
    file = os.getcwd()
    if not os.path.exists(path):
        nfile = open(path, "w")
        del nfile
    print(rotate(path))


rotate_log_file("naynesh.log")
'''

import logging
import time
from logging.handlers import RotatingFileHandler

def create_rotating_log(path):
    logger = logging.getLogger("Rotating Log")
    logger.setLevel(logging.INFO)
    handler = RotatingFileHandler(path, maxBytes=20, backupCount=5)
    logger.addHandler(handler)
    for i in range(10):
        logger.info("This is test log line %s" % i)
        time.sleep(1.5)

if __name__ == "__main__":
    log_file = "sample.log"
    create_rotating_log(log_file)
