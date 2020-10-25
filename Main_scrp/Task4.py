import os, os.path
abs_path = 'D:\Arduino'
data = os.listdir(abs_path)
all_subset = len(data)
files_only = len([name for name in data if os.path.isfile(abs_path+'\\'+name)])
sub_dir = all_subset - files_only
print("Number of files in directory:\n"+str(files_only)+"\n")
print("Number of sub-directories in directory:\n"+str(sub_dir)+"\n")
