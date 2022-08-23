
import os
from shutil import copyfile

# 图片存放的路径
path = r'C:\Users\64426\Desktop\source'
desPath =r'C:\Users\64426\Desktop\dest'

file_list = os.listdir(path)

def copy_func(file)

num = 1
for file in file_list:
    copyfile(os.path.join(path, file), os.path.join(desPath, file))
    num = num + 1
