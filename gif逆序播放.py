#   _*_ coding:utf-8 _*_
from PIL import Image, ImageSequence

imgname = 'C:\工作\gif动图逆序播放\科比投篮动图.'
im = Image.open(imgname + '.gif')
#   初始化列表
sequence = []
#在图像序列中遍历所有帧
i= 1
for f in ImageSequence.Iterator(im):
    sequence.append(f.copy())
    f.save(imgname + '分解'+ str(i) + '.png')#文件名需要有后缀，知道什么格式
    i += 1
#  将图像序列逆转
sequence.reverse()

#几张单的gif组合成动态图片
#im.save(out, save_all = True, append_images=[im1, im2......]),这边的im只需要是Image对象即可
sequence[0].save(r'C:\工作\gif动图逆序播放\动图逆序.gif', save_all=True, append_images=sequence[0:], duration=30)#sequence[0]为Image对象，[1][2]…都可以
