# 有一个目录装了很多照片 把它们的尺寸变成都不大于 iPhone5 分辨率的大小
# iPhone 5 屏幕分辨率：1136 * 640 （宽 x 高）

from PIL import Image
import os

__author__ = 'Alice'

def change_resolution(path):
    for picName in os.listdir(path):
    # 使用os.listdir()函数获得指定目录中的内容
        if picName != ".DS_Store":
            picPath = os.path.join(path,picName)
            with Image.open(picPath) as im:
                w,h = im.size
                n = w/1136 if (w/1136) >= (h/640) else h/640
                im.thumbnail((w/n,h/n))
                # thumbnail函数接受一个元组作为参数 分别对应缩略图的宽高
                # 在缩略时函数会保持图片的宽高比例
                im.save('finish_'+picName.split('.')[0]+'.jpg','jpeg')

if __name__ == '__main__':
    change_resolution('./pic')