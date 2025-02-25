import cv2
import numpy as np
from skimage.util import random_noise

class DataAugmentForObjectDetection():
    def __init__(self, add_noise_rate=0.5):
        self.add_noise_rate = add_noise_rate

    def _addNoise(self, img):
        '''
        输入:
            img:图像array
        输出:
            加噪声后的图像array
        '''
        return random_noise(img, mode='gaussian', seed=int(time.time()), clip=True) * 255

# 实例化数据增强类
dataAug = DataAugmentForObjectDetection()

# 读取图片
img = cv2.imread('path_to_your_image.jpg')

# 向图片添加高斯噪声
noisy_img = dataAug._addNoise(img)

# 显示或保存加噪声后的图片
cv2.imshow('Noisy Image', noisy_img)
cv2.waitKey(0)
cv2.destroyAllWindows()