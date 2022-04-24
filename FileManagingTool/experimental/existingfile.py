from glob import glob
import pathlib as pl
import os
import os.path
import time
import datetime
import shutil

#variables to sort folder by date and exteact data from subfolder
os.chdir("D:\experiment")# give here path : folder where we will perform opration 
filelist = list(os.listdir())# List the directories and make a list
dest = os.getcwd()# Get the current working directory
cfile=list(os.listdir(dest))#make list of file name 
fname=[]#to store only name of file for rename if file alredy exist
for i in cfile:
    t=os.path.basename(i)#it will retrun only file name 
    fname.append(t)#to append shorted name in list
# print(op)
def ExtractDataFromFolders():#to extract data from all subfolder in currunt folder
    for files in filelist: 
        try: 
            data = glob.glob(files+"\\*")#go to directory 
                             
            for f in data:# to check all the files inside the folder or directory
                sfile=os.path.basename(f)#to get basename of file xyz.jpg like this
                
                if sfile in fname:#compared two file from currunt directory to destination
                    global cout
                    pname,fext=os.path.splitext(f)#to split file name and extension for rename dubblicate
                    
                    newname=pname+"_copy"+fext
                    
                    shutil.move(f, newname)
                    print("Dublicate File Renamed To  :->",newname)
                else:               
                    shutil.move(f, dest)#to move file to target loctation   
                    print("File Moved To Destination :-.")
                        
            # shutil.rmtree(files)#to delete folder afeter  getting all data
        except:
            pass