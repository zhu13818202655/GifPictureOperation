import imageio
import os

gif = []
dir = 'C:\工作\gif动图逆序播放\合成gif动图素材'
for f in os.listdir(dir):
    imgname = dir + '\\' + f
    gif.append(imageio.imread(imgname))
gif_name = '周冬雨.gif'
imageio.mimsave(gif_name, gif, duration=0.1)