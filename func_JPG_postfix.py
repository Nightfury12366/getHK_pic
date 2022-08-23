import os
from tqdm import tqdm
from PIL import Image

dir_origin_path = r"C:\Users\64426\Desktop\2022_4_13_datasets\datasets\HK_project\train2020"
dir_save_path = r"C:\Users\64426\Desktop\2022_4_13_datasets\datasets\HK_project\train2020_b"

img_names = os.listdir(dir_origin_path)
for img_name in tqdm(img_names):
    if img_name.lower().endswith(('.bmp', '.dib', '.png', '.jpg', '.jpeg', '.pbm', '.pgm', '.ppm', '.tif', '.tiff')):
        image_path = os.path.join(dir_origin_path, img_name)
        image = Image.open(image_path)
        image = image.convert('RGB')

        if not os.path.exists(dir_save_path):
            os.makedirs(dir_save_path)
        image.save(os.path.join(dir_save_path, img_name))


