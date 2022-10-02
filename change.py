import re
import hashlib
import sqlite3
from db import *

def get_file_path():
    a = open("/etc/change-detector/change-detector.conf", "r+")
    files = []
    for i in a:
        if i == "" or i == "\n":
            continue
        try:
            filepath = re.search("(?<=FilePath ).*",i, re.MULTILINE)
            files.append(filepath[0])
        except:
            pass
    return files
def get_hash(files):
    hashFinal = []
    for i in files:
        HashFile = hashlib.md5(open(i.encode("utf-8"),"rb").read()).hexdigest()
        hashFinal.append(HashFile)
    return hashFinal
def main():
    con = sqlite3.connect("/etc/change-detector/change-detector.db")
    db = con.cursor()
    files = get_file_path()
    hashs = get_hash(files)
    for i in range(len(files)):
        insertFile( con , db , files[i] , hashs[i] )

