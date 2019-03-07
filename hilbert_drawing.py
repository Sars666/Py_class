'''
用turtle和希尔伯特曲线画图
代表"Poké Ball"精灵球
'''

import cv2
from turtle import *

#读取图片,输出rgb值与长宽
if __name__ == '__main__':
    img = cv2.imread("unknown.jpg")
    b, g, r = cv2.split(img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    size = img.shape

#位置对应的单RGB值
def colorIndex(color,position,picheight,picwidth,maxLength):
    return color[picheight-int((position[1]+150)*picheight/maxLength)-1][int(position[0]*picwidth/maxLength)-1]

#位置对应的RGB组
def poscolor(r,g,b,position,picheight,picwidth,maxLength):
    colortuple = colorIndex(r,position,picheight,picwidth,maxLength),\
                 colorIndex(g,position,picheight,picwidth,maxLength),\
                 colorIndex(b,position,picheight,picwidth,maxLength)
    return colortuple

def hilbert_curve(n, m):        #用迭代绘制希尔伯特曲线
    index=1
    if n == 1:                  #出栈条件
        pos = position()
        picheight = size[0]
        picwidth = size[1]
        maxLength = x*(2**pic_resolution)-x
        print(pos)
        color(poscolor(r,g,b,pos,picheight,picwidth,maxLength))
        fd(x)
        lt(180 * m - 90)
        fd(x)
        lt(180 * m - 90)
        fd(x)

    else:                       #迭代
        lt(180 * m - 90)
        hilbert_curve(n - 1, 1 - m)
        lt(180 * m - 90)
        fd(x)
        hilbert_curve(n - 1, m)
        lt(180 * m + 90)
        fd(x)
        lt(180 * m + 90)
        hilbert_curve(n - 1, m)
        fd(x)
        lt(180 * m - 90)
        hilbert_curve(n - 1, 1 - m)
        lt(180 * m - 90)

#画图初始化
def init():
    lt(90)
    penup()
    setposition(0,-150)
    pendown()

#初始化
title('希尔波特曲线')     #标题
speed(0)                #速度
pic_resolution = 5      #分辨率对应阶数
maxx = 320                  #最大步长
x = 320 / (2 ** pic_resolution) # 步长
hideturtle()            #隐藏指针
colormode(255)          #255rgb
pensize(x)
screensize(900, 600, "white")
setup(width=900, height=600)

#画标题
penup()
setposition(-420,200)
write('Poké Ball',font=("Arial",90,"normal"))
home()
pendown()


#画希尔伯特曲线
init()
hilbert_curve(pic_resolution, 0)
penup()
setposition(-400,-250)
pendown()
color('black')
write('click anywhere to exit',font=("Arial",50,"normal"))
exitonclick()
