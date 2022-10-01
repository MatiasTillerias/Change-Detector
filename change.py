import sqlite3
import re

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
    print(files)
def main():
        get_file_path()    
