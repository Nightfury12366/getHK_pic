# FilesBatchRename.py
# 导入os库
import os

# 图片存放的路径
path = r'C:\Users\64426\Desktop\验收数据集处理\白宫\美国白宫'

# 遍历更改文件名
num = 1
for file in os.listdir(path):
    os.rename(os.path.join(path, file), os.path.join(path, 'mgbg_22823_' + str(num))+".jpg")
    num = num + 1
