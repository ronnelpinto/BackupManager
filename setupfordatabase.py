import os
import pymysql as pm
import time
def acceptDir(): # method to find all the files in the given directory
	os.chdir(os.getenv("HOME")+'/Python - Lab')
	a=os.getcwd() #variable to hold current directory
	p=[]
	def get_files():
		for dirc,subs,files in os.walk(a): #os.walk recursive method to traverse the given directory
			for i in files:
			p.append([dirc,files]) #hold the path,files in p
	get_files()
	global q
	q=[]# p has repeatative entries, using q to hold single entry for each path
	for i in p:
		if i not in q:
			q.append(i)
	del p
	
def createDB():
	con = pm.connect(host='localhost',user="root",passwd='akkaa') #please replace 'akkaa' by your mysql password
	cur = con.cursor()
	cur.execute("create database if not exists backup")
	cur.execute("use backup")
	cur.execute("drop table if exists backList") # delete old table
	qry="create table backList(dir char(250),fname char(200), mtime DATE,hh int(2), min int(2),sec int(2))"
	cur.execute(qry) # create a fresh database
	for i in q: #for every file i in the given directory, structure of i: [path,[filenames]]
		os.chdir(i[0]) #change the directory to the path
		for j in i[1]: #for every file in the path
			yy,mm,dd,hh,mi,ss=map(int,(time.localtime(os.path.getmtime(j))[:6])) #gets last modification time
			cur.execute("insert into backList values (%s,%s,%s,%s,%s,%s)",(i[0],j,pm.Date(yy,mm,dd),hh,mi,ss)) #insert the info to the database
	con.commit()
	con.close()
	cur.close()
if __name__=='__main__':
	acceptDir()
	createDB()
