'''
    opencv数据增强
    对图片进行色彩增强、高斯噪声、水平镜像、放大、旋转、剪切
    并对每张图片随机保存其中的一种数据增强的图片
'''

# P图的AUG
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
    return dst
    # cv.imwrite(path_out, dst)


def gasuss_noise(image, path_out_gasuss, mean=0, var=0.00001):
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
    return out
    # cv.imwrite(path_out_gasuss, out)


def mirror(image, path_out_mirror):
    '''
        水平镜像
    '''
    h_flip = cv.flip(image, 1)
    return h_flip
    # cv.imwrite(path_out_mirror, h_flip)


def resize(image, path_out_large):
    '''
        放大两倍
    '''
    height, width = image.shape[:2]
    large = cv.resize(image, (2 * width, 2 * height))
    return large
    # cv.imwrite(path_out_large, large)


def rotate(image, path_out_rotate):
    '''
        旋转
    '''
    rows, cols = image.shape[:2]
    M = cv.getRotationMatrix2D((cols / 2, rows / 2), 10, 1)
    dst = cv.warpAffine(image, M, (cols, rows))
    return dst
    # cv.imwrite(path_out_rotate, dst)


def shear(image, path_out_shear):
    '''
        剪切
    '''
    height, width = image.shape[:2]
    crop_location_x = random.randrange(0, int(height / 8.7))
    crop_location_y = random.randrange(0, int(width / 8.7))

    cropped = image[int(crop_location_x):int(crop_location_x) + int(height * 8.7 / 10),
              int(crop_location_y):int(crop_location_y) + int(width * 8.7 / 10)]

    return cropped
    # cropped = image[int(height / 9):height, int(width / 9):width]
    # cv.imwrite(path_out_shear, cropped)


# 要进行增强的图像集合
image_path = r'D:\SkyLakeCode\Python\getHK_pic\pic_HK\tmp412'

# 一些模板图片，把它嵌入到图片中
mono_path = r'D:\SkyLakeCode\Python\getHK_pic\pic_HK\mono3'

# 输出的增强数据集合
image_out_path = r'D:\SkyLakeCode\Python\getHK_pic\pic_HK\proAug412'
if not os.path.exists(image_out_path):
    os.mkdir(image_out_path)
list = os.listdir(image_path)
mono_list = os.listdir(mono_path)  # 
print(mono_list)
imageNameList = [
    '_color.jpg',
    '_color.jpg',
    '_mirror.jpg',
    '_shear.jpg',
    '_gasuss.jpg',
    '.jpg',
    '.jpg'
    ]

#  注意这里改了，2022年4月12日修改
rName = "412_test_"

for i in range(0, len(list)):
    path = os.path.join(image_path, list[i])
    # print(path)
    out_image_name = os.path.splitext(list[i])[0]

    j = random.randrange(0, len(imageNameList))
    k = random.randrange(0, len(mono_list))

    s_path = os.path.join(mono_path, mono_list[k])
    # print(s_path)

    # path_out = os.path.join(image_out_path, out_image_name + imageNameList[j])
    path_out = os.path.join(image_out_path, rName + format(str(i), '0>3s') + '.jpg')

    image = cv.imread(path)
    s_img = cv.imread(s_path)
    if j == 0:
        s_img_ = contrast_brightness_image(s_img, random.uniform(1.0, 1.4), random.randrange(1, 10), path_out)
        print('contrast_brightness_image')
    elif j == 1:
        s_img_ = contrast_brightness_image(s_img, random.uniform(0.6, 1.0), random.randrange(-9, 0), path_out)
        print('contrast_brightness_image')
    elif j == 2:
        s_img_ = mirror(s_img, path_out)
        print('mirror')
    elif j == 3:
        s_img_ = shear(s_img, path_out)
        print('shear')
    elif j == 4:
        s_img_ = mirror(s_img, path_out)
        print('mirror')
    else:
        s_img_ = s_img
        print('ori')

    # print(s_img_.shape)
    img1_rows, img1_cols, img1_channels = image.shape
    # print(img1_rows, img1_cols, img1_channels)
    img2_rows, img2_cols, img2_channels = s_img_.shape
    img2 = cv.resize(s_img_, (int(img1_rows / 3), int(img2_rows / img2_cols * (img1_rows / 3))))
    img2_rows, img2_cols, _ = img2.shape

    x0 = random.randrange(int(img1_rows / 8), int(img1_rows / 4))
    y0 = random.randrange(int(img1_cols / 20), int(img1_cols / 1.5))
    image[x0:x0 + img2_rows, y0:y0 + img2_cols] = img2
    cv.imwrite(path_out, image)

