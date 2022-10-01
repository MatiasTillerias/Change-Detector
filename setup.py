import sqlite3
import os

os.mkdir("/etc/change-detector/")

conn = sqlite3.connect('/etc/change-detector/change-detector.db')
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS changes (
        id INTEGER PRIMARY KEY,
        file TEXT,
        hash TEXT
        )""")
conn.commit()
conn.close()

