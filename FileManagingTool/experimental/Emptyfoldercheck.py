
import os
import shutil
import glob
os.chdir("D:\experiment")#folder where we will perform opration
  

filelist = list(os.listdir())# List the directories and make a list

dest = os.getcwd()# Get the current working directory

cfile=list(os.listdir(dest))

for files in filelist:
    if len(os.listdir())==0:
        print("list is empty")
                        

    
    # try:
            
            
    #     data = glob.glob(files+"\\*")#go to directory

        
        
    #     if os.path.isdir(data):
    #         print("hfhdhd")
    #         if len(os.listdir(data)==0):
    #             print("trueeee")

    # except:
    #     pass


# if len((os.listdir(a) == 0:))# Check if the folder is empty
#     shutil.rmtree()