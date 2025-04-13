"""
#!/usr/bin/env python
# -*- coding:utf-8 -*-
@Project : code
@File : augmentation12222.py
@Author : Chenasuny
@Time : 2024/12/22 21:54
"""

import os
from PIL import Image, ImageEnhance

def low_light(image, factor=0.35):
    """降低图像亮度"""
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(factor)

def add_fog(image, factor=0.35):
    """添加雾化效果"""
    enhancer = ImageEnhance.Contrast(image)
    # 降低对比度以模拟雾化效果
    return enhancer.enhance(factor)

def process_images(input_folder, output_lowlight_folder, output_fog_folder):
    if not os.path.exists(output_lowlight_folder):
        os.makedirs(output_lowlight_folder)
    if not os.path.exists(output_fog_folder):
        os.makedirs(output_fog_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            image_path = os.path.join(input_folder, filename)
            with Image.open(image_path) as img:
                # 确保图像被加载
                img.load()

                # 保存低光处理后的图像
                lowlight_img = low_light(img)
                lowlight_save_path = os.path.join(output_lowlight_folder, filename)
                lowlight_img.save(lowlight_save_path)

                # 保存雾化处理后的图像
                fog_img = add_fog(img)
                fog_save_path = os.path.join(output_fog_folder, filename)
                fog_img.save(fog_save_path)

# 定义文件夹路径
input_folder = './test_set'
output_lowlight_folder = './lowlight'
output_fog_folder = './fog'

# 处理图像
process_images(input_folder, output_lowlight_folder, output_fog_folder)