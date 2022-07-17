
import os
origin_file_name = os.path.basename("./jsonLibManager.json")

ext_num = 0
file_name_num = 0
        
for i in origin_file_name:
    if (i != "."):
        file_name_num += 1
    else:
        break
    
file_ext = origin_file_name[file_name_num + 1: len(origin_file_name) + 1]
print(file_ext)
