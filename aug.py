'''
    opencv数据增强
    对图片进行色彩增强、高斯噪声、水平镜像、放大、旋转、剪切
    并对每张图片随机保存其中的一种数据增强的图片
'''
# -*- coding: utf-8 -*-
import shutil
import cv2 as cv
import os
import numpy as np
import random


def contrast_brightness_image(src1, a, g, path_out):
    '''
        色彩增强（通过调节对比度和亮度）
    '''
    h, w, ch = src1.shape  # 获取shape的数值，height和width、通道
    # 新建全零图片数组src2,将height和width，类型设置为原图片的通道类型(色素全为零，输出为全黑图片)
    src2 = np.zeros([h, w, ch], src1.dtype)
    # addWeighted函数说明:计算两个图像阵列的加权和
    dst = cv.addWeighted(src1, a, src2, 1 - a, g)
    cv.imwrite(path_out, dst)


def gasuss_noise(image, path_out_gasuss, mean=0, var=0.001):
    '''
        添加高斯噪声
        mean : 均值
        var : 方差
    '''
    image = np.array(image / 255, dtype=float)
    noise = np.random.normal(mean, var ** 0.5, image.shape)
    out = image + noise
    if out.min() < 0:
        low_clip = -1.
    else:
        low_clip = 0.
    out = np.clip(out, low_clip, 1.0)
    out = np.uint8(out * 255)
    cv.imwrite(path_out_gasuss, out)


def mirror(image, path_out_mirror):
    '''
        水平镜像
    '''
    h_flip = cv.flip(image, 1)
    cv.imwrite(path_out_mirror, h_flip)


def resize(image, path_out_large):
    '''
        放大两倍
    '''
    height, width = image.shape[:2]
    large = cv.resize(image, (2 * width, 2 * height))
    cv.imwrite(path_out_large, large)


def rotate(image, path_out_rotate):
    '''
        旋转
    '''
    rows, cols = image.shape[:2]
    M = cv.getRotationMatrix2D((cols / 2, rows / 2), 10, 1)
    dst = cv.warpAffine(image, M, (cols, rows))
    cv.imwrite(path_out_rotate, dst)


def shear(image, path_out_shear):
    '''
        剪切
    '''
    height, width = image.shape[:2]
    crop_location_x = random.randrange(0, int(height / 8.7))
    crop_location_y = random.randrange(0, int(width / 8.7))

    cropped = image[int(crop_location_x):int(crop_location_x) + int(height * 8.7 / 10),
              int(crop_location_y):int(crop_location_y) + int(width * 8.7 / 10)]

    # cropped = image[int(height / 9):height, int(width / 9):width]
    cv.imwrite(path_out_shear, cropped)


image_path = r'C:\Users\64426\Desktop\data_823\bg\mgbg'
image_out_path = r'C:\Users\64426\Desktop\data_823\bg\mgbg_out'
if not os.path.exists(image_out_path):
    os.mkdir(image_out_path)
list = os.listdir(image_path)
print(list)
imageNameList = [
    # '_color_up.jpg',
    # '_color_down.jpg',
    # '_mirror.jpg',
    '.jpg',
    '.jpg',
    '.jpg',
    '.jpg',
    '.jpg',
    '.jpg',
    '.jpg'
    ]

# 这一组图片重命名成什么名字

rName = "mgbg_22823_"

for i in range(0, len(list)):
    path = os.path.join(image_path, list[i])
    print(path)

    # out_image_name = os.path.splitext(list[i])[0]

    #  2022年4月11日修改
    out_image_name = rName + format(str(i), '0>3s')
    # 修改结束

    j = random.randrange(0, len(imageNameList))
    path_out = os.path.join(image_out_path, out_image_name + imageNameList[j])
    image = cv.imread(path)
    # if j == 0:
    #     contrast_brightness_image(image, random.uniform(1.2, 1.7), random.randrange(1, 10), path_out)
    # elif j == 1:
    #     contrast_brightness_image(image, random.uniform(0.4, 0.8), random.randrange(-9, 0), path_out)
    # elif j == 2:
    #     mirror(image, path_out)
    # else:
    shutil.copy(path, path_out)
