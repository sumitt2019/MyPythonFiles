import os
import shutil
from shutil import copy
from pathlib import Path
import time


#source directory of all input files to be combines
src = Path(r"C:\Users\username\Documents\Experiment\Input")
idx = 0

all_file = os.walk(src)


for folders, subfolders, filenames in all_file:
    for f in filenames:
        if f == 'Result.xlsx':
            time_f = time.ctime(os.path.getmtime(os.path.join(folders, f)))                   #Getting the last modification time of the file
            print(time_f)
            time_obj = time.strptime(time_f)                                                  #Creating the time object  
            print('Copying this file',os.path.join(folders, f))                               
            destination = r"C:\Users\username\Documents\Experiment\Output\Results"+str(time.strftime("%Y_%m_%d", time_obj)) + ".xlsx"                 #Giving the file name to the output file
            print(destination)
            shutil.copy2(os.path.join(folders, f), Path(destination))                                             
