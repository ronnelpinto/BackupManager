from tkinter import *
from tkinter import filedialog
from tkinter import messagebox as box
from backup import *
from setupfordatabase import *

class MainWIndow(Frame):        #the Main Frame class having instances of all the classes
    def __init__(self, parent):
        Frame.__init__(self, parent, background='#eed')
        self.parent = parent
        self.initUI()
        self.initQuitButton()
        self.initInputFolder()
        self.initExtension()
        self.initTargetFolder()
        self.initCompressionType()
        self.initLabels()
        self.initBackupButton()
        self.initInfoLabel()
        self.initScheduleButton()
        
    def initUI(self):        #initialising the UI
        self.parent.title('Linux Backup Manager')
        self.pack(fill=BOTH, expand=1)
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        self.parent.geometry('500x500+%d+%d' % ((sw - 100)/2, (sh - 100)/2))
        
    def initQuitButton(self):#initialises the Quit button
        quitButton = Button(self, text = "Quit", command = self.quit)
        quitButton.place(relx = 0.40, rely = 0.9, relwidth = 0.2)


    def initScheduleButton(self):#initialises the Schedule button
        quitButton = Button(self, text = "Schedule to run\n backup periodically\n on working directory", command = self.invokeScheduler)
        quitButton.place(relx = 0.20, rely = 0.7, relwidth = 0.5)    
        
    def initBackupButton(self):#initialises the Generate table button
        genButton = Button(self, text = "Backup", command = self.invokebackup)
        genButton.place(relx = 0.10, rely = 0.9, relwidth = 0.2)
        
        
    def initInputFolder(self, textParam=''):  #text area to enter input folder
        self.inputFolder = Text(self)
        self.inputFolder.place(relx = 0.05, rely = 0.15, relwidth = 0.6,relheight=0.08)
        self.inputFolder.insert(index = INSERT, chars = textParam)


    def initExtension(self, textParam=''):  #text area to enter Extension type
        self.Extension = Text(self)
        self.Extension.place(relx = 0.7, rely = 0.15, relwidth = 0.2,relheight=0.08)
        self.Extension.insert(index = INSERT, chars = textParam)

    def initTargetFolder(self, textParam=''):  #text area to enter target folder
        self.TargetFolder = Text(self)
        self.TargetFolder.place(relx = 0.05, rely = 0.5, relwidth = 0.6,relheight=0.08)
        self.TargetFolder.insert(index = INSERT, chars = textParam)


    def initCompressionType(self, textParam=''):  #text area to enter Compression type
        self.CompressionType = Text(self)
        self.CompressionType.place(relx = 0.7, rely = 0.5, relwidth = 0.2,relheight=0.08)
        self.CompressionType.insert(index = INSERT, chars = textParam)


                
    def initLabels(self):   #labels for the various uneditable fields
        l1 = Label(self, text = "The folder to be backed up\n(leave blank if current directory)", background='#eed')
        l2 = Label(self, text = "The target folder to save backups\n(leave blank if default backup folder)", background='#eed')        
        l11 = Label(self, text = "Mention extension if you want \nto backup files with a \nparticular extension", background='#eed')
        l22 = Label(self, text = "Compression type - tar or zip", background='#eed')
        l1.place(relx = 0.02, rely = 0.02, relwidth = 0.6)
        l2.place(relx = 0.02, rely = 0.4, relwidth = 0.6)
        l11.place(relx = 0.61, rely = 0.02, relwidth = 0.4)
        l22.place(relx = 0.61, rely = 0.4, relwidth = 0.4)
                
    def initInfoLabel(self, textParam = "Information: ", flag=1):   #info label to check for success or failure
        if flag is 1:
            l3 = Label(self, text = textParam, background='#3f3')
        else:
            l3 = Label(self, text = textParam, background='red')
        l3.place(relx = 0.79, rely = 0.70, relwidth = 0.2)    
        
    def invokebackup(self):
        #call to initialise code module of backup.py file
        check=len(self.Extension.get('0.0',END).strip("\n"))
        if check==0:
        	backup = initialise(str(self.inputFolder.get( '0.0', END)),'no',str(self.Extension.get( '0.0', END)),'all',str(self.TargetFolder.get( '0.0', END)),str(self.CompressionType.get( '0.0', END)))
        else: 
        	backup = initialise(str(self.inputFolder.get( '0.0', END)),'yes',str(self.Extension.get( '0.0', END)),'all',str(self.TargetFolder.get( '0.0', END)),str(self.CompressionType.get( '0.0', END)))
        
        if backup is 1:        #if backup is 1 then success else failure
            infoString = 'Success!\nThe files\n have been\nsuccessfully\nbacked up' 
            self.initInfoLabel(infoString, flag = 1)
        else:
            infoString = 'Error.\nThe files\n have not\nbacked up' 
            self.initInfoLabel(infoString, flag = 0)

    def invokeScheduler(self):  #code to call the Scheduler to schedule the backup of a particular working folder
        a=os.getcwd()
        acceptDir()
        createDB()
        os.chdir(a)
        os.system("python3 makeperiodic.py")
	
	
def main():     #main method to define the Tkinter interface
    root = Tk()
    app = MainWIndow(root)
    root.mainloop()
