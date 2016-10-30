print("A program that backs up a list of files/folders into a zip/tar archive")
import os
import time

source_dir=[]   #to store list of all files/folders in the directory
error_flag=1    #error flag to check if backup is successful or not

class Backup:
    def __init__(self,inputFolder,ext_flag,Extension,files,TargetFolder,CompressionType):
        self.inputFolder=inputFolder
        self.ext_flag=ext_flag
        self.Extension=Extension
        self.files=files
        self.TargetFolder=TargetFolder
        self.CompressionType=CompressionType
        source_dir=list(self.inputFolder)
        
    def implementation(self):
        cwd=self.inputFolder
        try:
                os.chdir(cwd) # Changes the working directory to the source's so that explicit declaration of directory not needed
        except:
                os.chdir(os.getcwd()) # If on present directory and the user doesn't give any input,
                cwd=os.getcwd() # natively assign cwd to the current directory itself
        print ('The list of files/folders present in',os.getcwd())

        direct=os.listdir(cwd)
        os.system('ls') # Gives the list of all files/folders so that user need not use a separate filemanager to know which
                              # files/folders to backup
                         
        if self.ext_flag =='yes' :
                flag=0 # taking a flag to know whether the user has given the correct extension
                dor=[] # creating an empty list to append the files that have the
                for ory in direct: # user's required extension
                        if str(self.Extension) in ory:
                                dor.append(ory)
                                flag = 1
                if flag == 0:
                        print ('Sorry!! No file with the specified extension exists.')
                        os.system('ls')
                else: # If flag is not 0, means it's 1 and that means the list 'dor' is not empty.
                        direct = dor[:] # which means it contains the list of filenames that end with the req extension
                        print ('Files with the extension %s are:' % self.Extension) # So the list 'dor' is copied to direct
                        for di in direct:
                                print (di,'\t')
                        print()

        if self.files == 'all':
                d=direct[:]
                strng=''
                for fold in d: # Let the list of all files/folders in the directory be backed up
                        strng = strng + ' ' + fold
                source_dir.append(strng)
                
        else:
                source_dir.append(s) # Only the files/folders specified by the user are backed up
                                                            
        arch=self.CompressionType

        # If you do not give target file then the default file 'backup' is taken to store the backup
        if len(str(self.TargetFolder)) == 0: # If the user has opted for me to generate a backup directory, I hav to create a target directory
                self.TargetFolder='/home/'+os.getlogin()+'/backup/' # Go to the user's home and create a folder for backups
                if not os.path.exists(self.TargetFolder): # (If it doesnt exist already)
                        os.mkdir(self.TargetFolder)
                today=self.TargetFolder+time.strftime('%Y%m%d')
                if not os.path.exists(today): # Create a subfolder for backups created today
                        os.mkdir(today) # assuming that user may back up more than one a day
                        print ('Backup folder created successfully @ %s' % today)
                        
                now=today+os.sep+time.strftime('%H%M%S')         #the time is added to distinguish each backup file
                
                comment="backup"
                
                if len(comment) == 0:
                        if arch=='zip':
                                target=now+'.zip'
                        else:
                                target=now+'.tar'
                else:
                        if arch=='zip': # Appending user's comments to the backup file
                                target=now+'_'+comment.replace(' ', '_')+'.zip'   #backup file name will have the date of the backup along with the supplementary comment
                        else:
                                target=now+'_'+comment.replace(' ', '_')+'.tar'
        else:
                comment="this is a backup"  #default comment to add to a backup file
                
                if len(comment) == 0:
                        if arch=='zip':
                                target=self.TargetFolder+time.strftime('%Y%m%d%H%M%S')+'.zip'  
                        else:
                                target=self.TargetFolder+time.strftime('%Y%m%d%H%M%S')+'.tar'
                else:
                        if arch=='zip':
                                target=self.TargetFolder+time.strftime('%Y%m%d%H%M%S')+'_'+comment.replace(' ', '_')+'.zip'
                        else:
                                target=self.TargetFolder+time.strftime('%Y%m%d%H%M%S')+'_'+comment.replace(' ', '_')+'.tar'

        print ('Backing up...')

        if arch=='zip':
                zip_command = "zip -qr '%s' %s" % (target, ' '.join(source_dir))
                if os.system(zip_command) == 0: # Running a terminal command via a program
                        print ('Backup Successful!! :)')
                        print ('Your backup file is @ %s' % target)    

                else:
                        print ('Backup Failed :(')
                        err=os.system(zip_command)
                        global error_flag
                        error_flag=0          #error flag is set to 0 mentioning that there was a error in the backup
                        print ('Error: ',err) #just returns the error number

        else:
                tar_command = "tar -czf %s %s" % (target, ' '.join(source_dir))
                if os.system(tar_command) == 0:
                        print ('Backup Successful!! :)')
                        print ('Your backup file is @ %s' % target)

                else:
                        print ('Backup Failed :(')
                        err=os.system(tar_command)
                        global error_flag
                        error_flag=0        
                        print ('Error: ',err)
                        

def initialise(inputFolder,ext_flag,Extension,files,TargetFolder,CompressionType):
    
    c=len(Extension.strip("\n"))   #check if user has specified an extension
    if c==0:
        ext_flag="no"              
    else:
        ext_flag="yes"
    a=Backup(inputFolder.strip("\n"),ext_flag.strip("\n"),Extension.strip("\n"),files.strip("\n"),TargetFolder.strip("\n"),CompressionType.strip("\n"))
    a.implementation()
    
    return error_flag           #return the error_flag to the gui code