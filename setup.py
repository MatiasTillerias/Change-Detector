import sqlite3
import os

try:
    os.mkdir("/etc/change-detector/")
except:
    pass

conn = sqlite3.connect('/etc/change-detector/change-detector.db')
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS changes (
        id INTEGER PRIMARY KEY,
        file TEXT,
        hash TEXT
        )""")
conn.commit()
conn.close()

