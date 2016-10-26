#coding=utf-8
'''
修改图片
By @liuxingpuu
'''

import random
from PIL import Image, ImageFont, ImageDraw

msgNum = str(random.randint(1,99))

im = Image.open('14.jpg')
w,h=im.size
wDraw=0.8*w
hDraw=0.08*w

font=ImageFont.truetype('/usr/share/fonts/truetype/droid/DroidSans.ttf', 130)
draw = ImageDraw.Draw(im)
draw.text((wDraw,hDraw),msgNum,font=font,fill=(255,0,0))

im.save ('14gai.jpg')
