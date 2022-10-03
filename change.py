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
    
    filesInDB = GeneralSelect(db,"file,hash")
    files = get_file_path()
    if len(filesInDB) == 0:
        hashs = get_hash(files)
        for i in range(len(files)):
            insertFile( con , db , files[i] , hashs[i] )
    else:
        dbfiles = []
        for i in filesInDB:
            dbfiles.append(i[0])
        diff = list(set(files) - set(dbfiles))
        if len(diff) >=1:
            newHash = get_hash(diff)
            print(newHash)
            for i in range(len(newHash)):
                insertFile(con,db,diff[i],newHash[i])
                
