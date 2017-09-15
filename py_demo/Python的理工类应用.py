# import numpy as np
# import pylab as pl
# x = np.linspace(-np.pi,np.pi,256)
# s = np.sin(x)
# c = np.cos(x)
# pl.title('Trigonometric Function')
# pl.xlabel('X')
# pl.ylabel('Y')
# pl.plot(x,s)
# pl.plot(x,c)
# pl.show()


# # 对一组数进行快速傅立叶变换
# import scipy as sp
# import pylab as pl
# listA = sp.ones(500)
# listA[100:300] = -1
# f = sp.fft(listA)
# pl.plot(f)
# pl.show()


# python图像处理库：Pillow（PIL）、OpenCV、Skimage
from PIL import Image
im1 = Image.open('1.jpg')
print(im1.size,im1.format,im1.mode)
Image.open('1.jpg').save('2.png')
im2 = Image.open('2.png')
size = (288,180)
im2.thumbnail(size) # 缩略图
im2.save('2.png')
out = im2.rotate(45) # 逆时针旋转45度角
im1.paste(out,(50,50))
im1.save('1.jpg')

# from Bio.Seq import Seq
# my_seq = Seq("AGTACACTGGT")
# print(my_seq.alphabet)
# print(my_seq)
