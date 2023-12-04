import os 
import shutil
from_dir="C:/Users/SARAF/Downloads"
to_dir="C:/Users/SARAF/OneDrive/Desktop/Downloads"
list_dir=os.listdir(from_dir)
print(list_dir)
for file_name in list_dir:
    name,extension=os.path.splitext(file_name)
    print(name)
    print(extension)
    if extension =='':
        continue
    if extension in [".pdf"]:
        path1=from_dir+"/"+file_name
        path2=to_dir+"/"+"pdf"
        path3=to_dir+"/"+"pdf"+"/"+file_name
        if(os.path.exists(path2)):
          shutil.move(path1,path3)
        else:
           os.makedirs(path2)
           shutil.move(path1,path3)