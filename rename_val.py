import os

# file = open('ll.txt')
# dataMat = []
#
# for line in file.readlines():
#     curLine = line.strip().split(" ")
#     floatLine = map(float, curLine)  # 这里使用的是map函数直接把数据转化成为float类型
#     dataMat.append(floatLine[0:2])
#     labelMat.append(floatLine[-1])

# 重命名
import os

imgs_path = r'C:\Users\64426\Desktop\mmm\img'
vals_path = r'C:\Users\64426\Desktop\mmm\val'
imgs = os.listdir(imgs_path)
vals = os.listdir(vals_path)

imgs.sort()
vals.sort()
print(imgs)
print(vals)
i = 0
j = 0
for img in imgs:
    # images = os.listdir(format(str(file)))
    # print(images)
    src = os.path.join(imgs_path, img)
    dst = os.path.join(imgs_path,
                       '_J' + format(str(i), '0>3s') + '.jpg')
    os.rename(src, dst)
    print('Converting %s to %s ...' % (src, dst))

    # -------------------------------------------------------------------
    i = i + 1

for val in vals:
    # images = os.listdir(format(str(file)))
    # print(images)
    src = os.path.join(vals_path, val)
    dst = os.path.join(vals_path,
                       '_J' + format(str(j), '0>3s') + '.xml')
    os.rename(src, dst)
    print('Converting %s to %s ...' % (src, dst))

    # -------------------------------------------------------------------
    j = j + 1
