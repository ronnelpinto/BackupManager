print("Python program to back up a list of files/folders into a zip or tar archive")
import os
import time

source_dir = []   # list of all files/folders
error_flag = 1    # error flag for backup

class Backup:
    def __init__(self,inputFolder,ext_flag,Extension,files,TargetFolder,CompressionType):
        self.inputFolder = inputFolder
        self.ext_flag = ext_flag
        self.Extension = Extension
        self.files = files
        self.TargetFolder = TargetFolder
        self.CompressionType=  CompressionType
        source_dir = list(self.inputFolder)

        
    def implementation(self):
        cwd = self.inputFolder
        try:
                os.chdir(cwd) # Changes the working directory to source
        except:
                os.chdir(os.getcwd()) # If on present directory and no user input, then assign cwd to the current directory
                cwd = os.getcwd()
        print ('The list of files/folders present in ', os.getcwd())

        cur_dir = os.listdir(cwd)
        os.system('ls') # Gives the list of all files/folders
                         
        if self.ext_flag =='true' :
                flag = 0 # flag for correct extension check
                dor = [] # empty list to append the files that have the user's extensions
                for item in cur_dir:
                        if str(self.Extension) in item:
                                dor.append(item)
                                flag = 1
                if flag == 0:
                        print ('Sorry, No file with the specified extension exists in the selected directory.')
                        os.system('ls')
                else: # If flag is not 0, means it's 1 and that means the list 'dor' is not empty.
                        cur_dir = dor[:] # which means it contains the list of filenames that end with the req extension
                        print ('Files with the extension %s are:' % self.Extension) # So the list 'dor' is copied to direct
                        for di in cur_dir:
                                print (di,'\t')
                        print()

        if self.files == 'all':
                d = cur_dir[:]
                file_list=''
                for fold in d: # Let the list of all files/folders in the directory be backed up
                        file_list = file_list + ' ' + fold
                source_dir.append(file_list)
                
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
                comment="This is a backup"  #default comment to add to a backup file
                
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
                        print ('Backup Successful!')
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
        ext_flag="false"
        print ('User has not specified extension - Use default')
    else:
        ext_flag="true"
    a=Backup(inputFolder.strip("\n"),ext_flag.strip("\n"),Extension.strip("\n"),files.strip("\n"),TargetFolder.strip("\n"),CompressionType.strip("\n"))
    a.implementation()
    
    return error_flag           #return the error_flag to the gui code
