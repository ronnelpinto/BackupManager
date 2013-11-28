from selectfromdb import *
def if_modified():
	for i in modified: # i has details of modified file, path,filename
		source_dir=i[1]
		os.chdir(i[0])
		target_dir='/home/'+os.getenv("USER")+'/backup/' #to create a directory -backup if doesn't exist
		if not os.path.exists(target_dir):
			os.mkdir(target_dir)
		today=target_dir+time.strftime('%Y%m%d') # to create sub directory with current date
		if not os.path.exists(today):
			os.mkdir(today)
		now=today+os.sep+time.strftime('%H%M%S')
		target=now+i[1]+'.zip' #file name of the backup file
		zip_command = "zip -qr '%s' %s" % (target, source_dir) #Linux command to create zip file
		if os.system(zip_command) == 0: # Running a terminal command via a program
			print ('Backup Successful!! for',i)
def back_up_again(): # method to backup for every modified 
	retrievefrmDB()
	if modified:
		#print(modified)
		if_modified()
		con = pm.connect(host='localhost',user="root",passwd='akkaa') #replace 'akkaa' by your mysql password
		cur = con.cursor()
		#cur.execute("create database if not exists backup")
		cur.execute("use backup")
		for i in modified: # for every modified file update the database with lastest last modified time
			os.chdir(i[0])
			yy,mm,dd,hh,mi,ss=map(int,(time.localtime(os.path.getmtime(i[1]))[:6])) #get the last modified time
			qry="delete from backList where dir=\""+i[0]+"\" and fname=\""+i[1]+"\""
			cur.execute(qry)
			cur.execute("insert into backList values (%s,%s,%s,%s,%s,%s)",(i[0],i[1],pm.Date(yy,mm,dd),hh,mi,ss))
		con.commit()
		con.close()
		cur.close()
back_up_again()
