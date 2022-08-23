# coding=utf-8
import xml.etree.ElementTree as ET
import os
import json
import argparse
import urllib
import yaml

# 重命名XML里头的图片名称
def getimages(xmlname):
    tree = ET.parse(xmlname)  # 输入是指定的xml文件，包括路径！
    rename = xmlname.split('/')[-1].split('.')[0]  #
    root = tree.getroot()

    for i in root:  # 遍历一级节点
        if i.tag == 'filename':  # 图片名
            file_name = i.text  # 0001.jpg
            # print(file_name)
            i.text = rename + '.' + file_name.split('.')[-1]
            # print(i.text)
        if i.tag == 'path':
            file_name = i.text  # 0001.jpg
            i.text = rename + '.jpg' # + file_name.split('.')[-1]

    tree.write(xmlname, 'UTF-8')


file_path = 'C:/Users/64426/Desktop/mmm/val/'
file_list = os.listdir(file_path)
# print(len(file_list))
for file in file_list:
    print(file_path+file)
    getimages(file_path+file)
# getimages(filename)