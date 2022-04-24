from glob import glob
import pathlib as pl

from rich.progress import track
import os
import os.path
import time
import datetime
import shutil
import glob
import colorama
from colorama import Fore ,Back,Style
colorama.init(autoreset=True)#this will inisilize module for color code

#varibales to sort data by extenstion
mod=""
file=[]   #empty list to store files
ext=set() #empty set to store extentions
inpath=""   #empty string to store path which gived by user



#variables to sort folder by date and exteact data from subfolder
mainpath=input("Give Path For Operation :-> ")
os.chdir(mainpath)# give here path : folder where we will perform opration 
filelist = list(os.listdir())# List the directories and make a list
dest = os.getcwd()# Get the current working directory
cfile=list(os.listdir(dest))#make list of file name 
fname=[]#to store only name of file for rename if file alredy exist
for i in cfile:
    t=os.path.basename(i)#it will retrun only file name 
    fname.append(t)#to append shorted name in list
# print(op)
def ExtractDataFromFolders():#to extract data from all subfolder in currunt folder
    for files in track(filelist) : 
        try: 
            data = glob.glob(files+"\\*")#go to directory 
                             
            for f in track(data):# to check all the files inside the folder or directory
                sfile=os.path.basename(f)#to get basename of file xyz.jpg like this
                
                if sfile in fname:#compared two file from currunt directory to destination
                    global cout
                    pname,fext=os.path.splitext(f)#to split file name and extension for rename dubblicate
                    
                    newname=pname+"_copy"+fext
                    
                    shutil.move(f, newname)
                    print(f"{Fore.RED},Dublicate File Renamed To  :->",newname)
                else:               
                    shutil.move(f, dest)#to move file to target loctation   
                    print(f"{Fore.GREEN}File Moved To Destination :->",f)
                        
            # shutil.rmtree(files)#to delete folder afeter  getting all data
        except:
            pass
def SortByDate():
    for files in track(os.listdir('.')):     
        # To get all the details of the file creation and modification
        gettime= time.gmtime(os.path.getmtime(files))      
        # extract only the Year, Month, and Day
        timebydate = datetime.datetime.strptime(str(gettime.tm_mon), "%m")
        
        # Provide the number and find the month
        month = timebydate.strftime(
            "%b")
        
        # Give the name of the folder
        folder = month + '-' + \
            str(gettime.tm_mday) + "-" + \
            str(gettime.tm_year)

        try:
            if files in os.listdir(folder):
                
                pname,fext=os.path.splitext(files)#to split file name and extension for rename dubblicate
                        
                newname=pname+"_copy"+fext
                        
                shutil.move(files, newname)
                print(f"{Fore.RED}{files} Renamed...")
        except:
            pass
        # To Check the folder exists or not
        if not os.path.isdir(folder):
            # If not then make the new folder
            os.mkdir(folder)
        sendto = folder

        print(f"{Fore.RED}File Name:",files)
        print(f"{Fore.BLUE}Sending to :",sendto)
        
        #To check wheter is file or not if it is file it will retrun true
        if os.path.isfile(files):
             
        # Move all the files to their destination folder folders
            shutil.move(files, sendto)  
    print(f"{Fore.GREEN}File has been sorted ......")

def GetExtention():
    global ext
    for i in file:
        if i.is_file():#it will check is a file or directory in given path if it is file it will retrun true
            
            ext.add(i.suffix.replace(".",""))#it will add all extention inside set .jpg.png  and .replce funtion will replace "." into "" jpg png

def SetFolder(value):#value to make folders in set or list which we make ext it is set having all extension
    for i in value:
        # print(nameordate)

        try:
            os.mkdir(inpath /i ) #it will make  new folders inside path directory
            
        except:
            pass
def MoveFile():
    for i in track(file):
        try:
            os.rename(i,inpath/i.suffix.replace(".","")/i.name)# it will move file to destionation folder
            if i.suffix.replace(".","") not in i:#to replace the file ext "." into ""
                os.mkdir(inpath/"other")#to make path
                os.rename(i,inpath/"other"/i.name)#move file to destination folder
        except:
            pass
    
    print(f"{Fore.GREEN}File Sorted......")

def Start():
    global inpath,file
    inpath=pl.Path(mainpath)#it will get path of all files 
    for i in inpath.glob("*"): #glob funtion will select all files form path and show 
        
        file.append(i)#this will append all file inside list :flie[]:



    GetExtention() #fution to get app extensions inside set()
    SetFolder(ext)#pass the input to setfolders
    MoveFile()#funtion to move files to destnation folder
    

if __name__=="__main__":
    print(f'''{Fore.RED}

    

    ####    ##    ##    #########
    #       # #  # #        #
    #       #   #  #        #
    ####    #      #        #
    #       #      #        #
    #       #      #        # 
{Fore.BLUE}
 Files{Fore.GREEN}      Managing{Fore.YELLOW}      Tool
    ''')



    print(f'''{Fore.YELLOW}
    
******Choose Number For Operation******

{Fore.RED}    1-> Manage File By Type
{Fore.BLUE}    2-> Manage File By Date Of Creation
{Fore.YELLOW}    3-> Manage File By Extensions
{Fore.GREEN}    4-> Extract File From  Sub Folders To Currant Folder 
{Fore.YELLOW}
****************************************   
            ''')

    user=int(input(f"{Fore.MAGENTA}Which Operation Do You Want To Performe :"))
    if user==1:
        print(f"{Fore.GREEN}Feature will add soonn....")

    elif user==2:
        SortByDate()
        print(f"{Fore.GREEN}Operation Finised...")
    elif user==3:
        Start()
        print(f"{Fore.GREEN}Operation Finised...")
    elif user==4:
        ExtractDataFromFolders()
        print(f"{Fore.BLUE}Operation Finised...")



