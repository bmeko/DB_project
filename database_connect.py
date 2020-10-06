import pymysql as sql 

db=sql.connect("localhost", "root" , "lab123", "DEC_CIT")
cursor = db.cursor()



class sqldb(object):
	def registration(fname,lname,email,password,phone,position):
		if position =='RESEARCHER':
			sql = """INSERT INTO `temp`(`first_name`,`last_name`,`email`,`password`,`phone`)
			VALUES ('{}','{}','{}','{}','{}')""".format(fname,lname,email,password,phone) 

		try:
			cursor.execute(sql)
			db.commit()
		except:
			db.rollback()
		db.close()



	def confirmation():
