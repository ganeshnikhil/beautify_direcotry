

import os 
import math
path=os.getcwd()

total_files=0
total_directories=0
space_consumed=0
for dirpath,dirnames,filenames in os.walk(path):
   total_files+=len(filenames)
   total_directories+=len(dirnames)
   directory_level=dirpath.replace(path,"")
   directory_level=directory_level.count(os.sep)
   indent="."*3
   print(f"|{indent*directory_level}|-\{os.path.basename(dirpath)}")
   
   
   for f in filenames:
      size_path=dirpath+'/'+f 
      files_stats=os.stat(size_path)
      file_size=files_stats.st_size/(1024*1024)
      size_unit='MB'
      space_consumed+=file_size
      
      
      if file_size<1:
         file_size=(file_size*(1024*1024))*0.001
         size_unit='KB'
      print(f"|{indent*(directory_level+3)}| - |__{f} {round(file_size,2)} {size_unit}")

print(f"[+]Total_Cur_Dir_Files:{len(os.listdir(path))}")
print(f"[+]Total_Files:{total_files}")
print(f"[+]Total_Directories:{total_directories}")
print(f"[+]Total Space in use:{math.ceil(space_consumed)} MB")