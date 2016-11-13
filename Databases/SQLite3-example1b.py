while 0==0:
	import sqlite3
	
	dbn = raw_input("DATABASE NAME:  ")+'.db'
	sql = sqlite3.connect(dbn).cursor()

	sql.execute(raw_input("SQL QUERY:  "))
	print sql.fetchall()
	#SHOW TABLES: select name from sqlite_master where type = 'table'
	sqlite3.connect(dbn).close()
