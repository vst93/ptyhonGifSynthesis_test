#-*- coding: UTF-8 -*-
#!/usr/bin/python3

import imageio
import time
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def changet_png(image_name,str):
    fnt=ImageFont.truetype('FZXBSJW.TTF', 21)
    im = Image.open(image_name).convert('RGBA')
    #新建一个图片，尺寸与上面的尺寸一样，透明度为0即完全透明
    txt=Image.new('RGBA', im.size, (0,0,0,0))
    #设置要写文字的字体，注意有的字体不能打汉字,这里用的微软雅黑可以
    #打汉字
    d=ImageDraw.Draw(txt)
    #写要打的位置，内容,用的字体，文字透明度
    d.rectangle([(0,txt.size[1]-40 ), (txt.size[0], txt.size[1])],fill=(255,255,255))
    d.text((0,txt.size[1]-30),str,font=fnt, fill=(0,0,0))
    #两个图片复合
    out=Image.alpha_composite(im, txt)
    #保存加水印后的图片
    out.save(image_name)

def create_gif(image_list, gif_name,str):

    list1 = [8,15];
    # Save them as frames into a gif

    frames = []
    i = 0
    for image_name in image_list:
        if i>=8 and i<=15:
            changet_png(image_name,' 别做'+str+'开发了好吗')
        elif i>=39:
            changet_png(image_name,'   '+str+'有那么好玩吗')

        frames.append(imageio.imread(image_name))
        i += 1

    imageio.mimsave(gif_name, frames, 'GIF', duration = 0.2)

    return

def main(replace_str=''):
    png_dir_name = 'webwxgetms01'
    image_list = []
    for i in range(55):
        image_list.append('webwxgetms01/webwxgetms01-'+ str(i) +'.png')

    gif_name = png_dir_name+'-'+replace_str +'.gif'
    # print(image_list)
    # exit()
    create_gif(image_list, gif_name,replace_str)
    return

if __name__ == "__main__":
    main()
