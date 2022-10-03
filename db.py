def insertFile( con , db , filePath , hashValue ):
    db.execute("INSERT INTO changes (file, hash) values (?,?)", (filePath,hashValue))
    con.commit()
    return
def GeneralSelect(db,row):
    db.execute(f"SELECT {row} FROM changes")
    return db.fetchall()
