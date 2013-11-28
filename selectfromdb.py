import os
import pymysql as pm
import time
modified=[] # to hold list of modified file details
def retrievefrmDB():
	#address of directory which needs to be looked up periodically and create backup for every modified file
	os.chdir(os.getenv("HOME")+'/Python - Lab')
	con = pm.connect(host='localhost',user="root",passwd='akkaa') #connect to the database, replace 'akkaa' by your mysql password
	cur = con.cursor()
	cur.execute("use backup") # get into 'backup' database
	qry="select * from backList"
	cur.execute(qry) # querry against the database to retrieve all the file information
	myList=cur.fetchall() # to list the files in myList
	global modified
	# for every file i in myList: components of i : path_of_file, filename, date_of_last_modification, time_of_modification
	for i in myList:
		try:
			os.chdir(i[0]) # change the current working directory to the file's directory
			yy,mm,dd,hh,mi,ss=map(int,(time.localtime(os.path.getmtime(i[1]))[:6])) #get the lastest modified time using os module; convert it into time structure and retrieve in corresponding fields
			yy1,mm1,dd1=i[2].timetuple()[:3] # data from database
			hh1,mi1,ss1=i[3:]
			if(yy>yy1 or (yy==yy1 and mm>mm1)or(yy==yy1 and mm==mm1 and dd>dd1)\
			or(yy==yy1 and mm==mm1 and dd==dd1 and hh>hh1)or(yy==yy1 and mm==mm1 and dd==dd1 and hh==hh1 and mi>mi1)\
			or(yy==yy1 and mm==mm1 and dd==dd1 and hh==hh1 and mi==mi1 and ss>ss1)):
				modified.append([i[0],i[1],yy,mm,dd,hh,mi,ss]) #check if any changes in modified time, if so append to list of modified files
		except Exception as e:
			print(e,type(e))

