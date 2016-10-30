from gui import *;

#Usn, name and summary

try:
    main() #The main method which invokes the GUI thus starting the execution
except Exception as e: #appropriate error handling to deal with unexpected runtime errors
    print(e)
finally:
    print("Program successsfully executed")