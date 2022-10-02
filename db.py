def insertFile( con , db , filePath , hashValue ):
    db.execute("INSERT INTO changes (file, hash) values (?,?)", (filePath,hashValue))
    con.commit()
    return 
