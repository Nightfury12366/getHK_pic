import glob
import cv2
import os
from PIL import Image
import os.path as osp
from pylab import *


def file_name(fd):  # 返回文件夹中的所有文件名
    L = []
    for root, dirs, files in os.walk(fd):
        for file in files:
            L.append(os.path.join(root, file))
        return L


path = r"C:\Users\64426\Desktop\data_823"
landmark = '大楼_VIDEO'
savemark = '大楼_FPS'
file_dir = r'C:\Users\64426\Desktop\data_823'

videoL = file_name(osp.join(file_dir, landmark))
print(videoL)

for video in videoL:
    cap = cv2.VideoCapture(video)
    v_n = video.split('\\')[-1].split('.')[0]  # 视频名字
    size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    # fps = int(cap.get(cv2.CAP_PROP_FPS))
    # print(fps)
    fps = 30
    save_dir = osp.join(path, savemark)  # 定位到图片保存目录
    if not osp.exists(save_dir):  # 不存在这个文件夹就新建一个
        os.makedirs(save_dir)
    index = 0
    while cap.isOpened():
        ret, frame = cap.read()  # ret是bool型，当读完最后一帧就是False，frame是ndarray型
        if not ret:  # 读完结束
            break
        # frame_new = cv2.resize(frame, size)
        # print(index)
        if index % fps == 0:  # 1秒提取一帧
            cv2.imencode('.jpg', frame)[1].tofile(os.path.join(save_dir, str(v_n)+'_'+str(index)+'.jpg'))  # 路径含中文存图
        index += 1
        # cv2.imshow("N M S L", frame)
        # cv2.waitKey(1)

    cap.release()
