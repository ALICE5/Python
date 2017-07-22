#将头像右上角加上红色的数字 类似微信未读信息的提示效果

#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'Alice'

from PIL import Image,ImageDraw,ImageFont,ImageFilter
#PIL是Python下非常强大的处理图像的工具库 Pillow是基于PIL的项目
#PIL的ImageDraw提供了一系列绘图方法 可以直接绘图
import random

picNum = str(random.randint(1,100))

#Read Image
im = Image.open('pic.jpg')
w,h = im.size
wDraw = 0.85 * w
hDraw = 0.04 * h

#Draw Image
font = ImageFont.truetype('/System/Library/Fonts/MarkerFelt.ttc',25)
#ImageFont.truetype(file,size)
#从指定的文件加载了一个字体对象 并且指定了大小25
draw = ImageDraw.Draw(im)
#创建一个可用来对image进行操作的对象
draw.ellipse([168,3,198,33],fill="red")
#画圆
draw.line([0,im.size[1],im.size[0],0],fill=128) #size第一个参数存储宽 第二个参数存储高
draw.line([0,0,im.size[0],im.size[1]],fill=128)
#画两条对角线
draw.text((wDraw,hDraw),picNum,font=font,fill=(255,255,255))
#在显示的图片中 输出文字 font为字体对象

#Save Image
im = im.filter(ImageFilter.BLUR)
#添加模糊效果
im.save('pic_num.jpeg','jpeg')