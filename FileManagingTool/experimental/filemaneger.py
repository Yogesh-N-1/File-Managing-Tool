from glob import glob
import pathlib as pl
import os
import os.path
import time
import datetime
import shutil


#location where to  store file
os.chdir("D:\experi2")
#list of directory inside list
filelist=list(os.listdir())   
# to get currunt working directory
cwd=os.getcwd() 
mod=""
file=[]   #empty list to store files
ext=set() #empty set to store extentions
path=""   #empty string to store path which gived by user

def moveFileByDate():
    for file in filelist:
        
        try:
            filedata=pl.glob(file+"\\*")
            print("this is file data",filedata)
            print("here")
            for mfile in filedata:
                
                shutil.move(mfile,cwd)
                
            shutil.rmtree(file)

        except:
            pass

    for file in os.listdir('.'):
        print("list dir",os.listdir)
         # and modification
        time_format = time.gmtime(os.path.getmtime(file))
        
        # Now, extract only the Year, Month, and Day
        datetime_object = datetime.datetime.strptime(str(time_format.tm_mon), "%m")
        
        # Provide the number and find the month
        full_month_name = datetime_object.strftime("%b")
        
        # Give the name of the folder
        mod = full_month_name + '-' + \
            str(time_format.tm_mday) + "-" + \
            str(time_format.tm_year)
        if not os.path.isdir(mod):
            print(mod)
            print("i am in mkdir")

            
            os.mkdir(mod)
            
        sendto=mod
        shutil.move(file,sendto)

        print("movied")

def GetExtention():
    global ext
    for i in file:
        if i.is_file():#it will check is a file or directory in given path if it is file it will retrun true
            
            ext.add(i.suffix.replace(".",""))#it will add all extention inside set .jpg.png  and .replce funtion will replace "." into "" jpg png
# def GetDateTime():
#     global mod,dateofflie

#     for i in file:
#         if i.is_file():
#             a=str(i)
#             b=a.replace("WindowsPath","").replace("(","").replace(")","")
#             # print(a)
#             created=os.path.getctime(b)
            
#             mod= time.strftime('%Y-%m-%d ',time.localtime(created))
#             dateoffile.add(mod)
#             print(mod)
#         # print(mod)
#     # print(dateoffile)


def SetFolder(value):#value to make folders in set or list which we make ext it is set having all extension
    for i in value:
        # print(nameordate)

        try:
            os.mkdir(path /i ) #it will make  new folders inside path directory
            
        except:
            pass
def Movefile():
    for i in file:
        try:
            os.rename(i,path/i.suffix.replace(".","")/i.name)# it will move file to destionation folder
            if i.suffix.replace(".","") not in i:
                os.mkdir(path/"other")
                os.rename(i,path/"other"/i.name)
        except:
            pass
    
    print("Filed Sorted......")       
# # def Movefilebydate():    
#     for f in file:
#         if f.is_file():
#             pathd=str(dateoffile)
            
#             try:
#                 new_path = os.path.join(path, pathd)
#                 src_path = os.path.join(path, f)
#                 shutil.copy(src_path, new_path)
#             except:
#                 pass
            
#         # try:
        #     a=str(i)
        #     b=a.replace("WindowsPath","").replace("(","").replace(")","")
        #     # os.rename(i,path/mod/i.name)# it will move file to destionation folder
        #     print(mod)
        #     os.rename(i,path/mod/i.name)
        #     print("moved")
        # if i.is_file():
            
        #     print("this is i",i.name)
        #     a=str(i)
        #     b=a.replace("WindowsPath","").replace("(","").replace(")","")
            
        #     created=os.path.getctime(b)
        #     mod2= time.strftime('%Y-%m-%d ',time.localtime(created))
        #     print(mod2)
        #     try:
        #         os.replace(i,path/dateoffile/i.name)
        #         print("moved")
        #     except:
        #         pass
def fun():

	# Change the directory and jump to the location
	# where you want to arrange the files
	os.chdir("D:\experiment")

	# List the directories and make a list
	all_files = list(os.listdir())

	# Get the current working directory
	outputs = os.getcwd()

	# Run a loop for traversing through all the
	# files in the current directory
	for files in all_files:
		try:
			
			# Jump to the directories files
			inputs = glob.glob(files+"\\*")
			
			# Now again run a loop for travering through
			# all the files inside the folder
			for ele in inputs:
				
				# Now, move the files one-by-one
				shutil.move(ele, outputs)
			
			# After extracting files from the folders,
			# delete that folder
			shutil.rmtree(files)
		except:
			pass

	# Again run a loop for traversing through all the
	# files in the current directory
	for files in os.listdir('.'):
		
		# Get all the details of the file creation
		# and modification
		time_format = time.gmtime(os.path.getmtime(files))
		
		# Now, extract only the Year, Month, and Day
		datetime_object = datetime.datetime.strptime(str(time_format.tm_mon), "%m")
		
		# Provide the number and find the month
		full_month_name = datetime_object.strftime("%b")
		
		# Give the name of the folder
		dir_name = full_month_name + '-' + \
			str(time_format.tm_mday) + "-" + \
			str(time_format.tm_year)

		# Check if the folder exists or not
		if not os.path.isdir(dir_name):
			
			# If not then make the new folder
			os.mkdir(dir_name)
		dest = dir_name
		
		# Move all the files to their respective folders
		shutil.move(files, dest)
		
	print("successfully moved...")
def Start():
    global path,file
    path=pl.Path(input("Enter path of files :"))#it will get path of all files 
    for i in path.glob("*"): #glob funtion will select all files form path and show 
        
        file.append(i)#this will append all file inside list :flie[]:
    GetExtention() 
    
    # GetDateTime()
    SetFolder(ext)#pass the input to setfolders
    Movefile()
    
    #Movefilebydate()
if __name__=="__main__":
    Start()
