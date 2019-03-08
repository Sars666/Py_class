'''
用turtle和希尔伯特曲线画图
代表"Poké Ball"精灵球
'''

import cv2
from random import randint
from turtle import *

#随机选取图片
nameList = ['Pokeball','Minecraft','creeper','hasaki',
            'heart','view']
randomIndex = randint(0,len(nameList)-1)
print(randomIndex)
name = nameList[randomIndex]
print(name)
filename = name + '.jpg'
#读取图片,输出rgb值与长宽
if __name__ == '__main__':
    img = cv2.imread(filename)
    b, g, r = cv2.split(img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    size = img.shape

#位置对应的单RGB值
def colorIndex(color,position,picheight,picwidth,maxLength):
    return color[picheight-int((position[1]+150)*picheight/maxLength)-1]\
        [int((position[0]+300)*picwidth/maxLength)-1]

#位置对应的RGB组
def poscolor(r,g,b,position,picheight,picwidth,maxLength):
    colortuple = colorIndex(r,position,picheight,picwidth,maxLength),\
                 colorIndex(g,position,picheight,picwidth,maxLength),\
                 colorIndex(b,position,picheight,picwidth,maxLength)
    return colortuple

def setPositionColor():
    pos = position()
    picheight = size[0]
    picwidth = size[1]
    maxLength = x*(2**pic_resolution)-x
    print(pos)
    color(poscolor(r,g,b,pos,picheight,picwidth,maxLength))

#用迭代绘制希尔伯特曲线
def hilbert_curve(n, m):
    #出栈条件
    if n == 1:
        setPositionColor()
        fd(x)
        lt(180 * m - 90)
        fd(x)
        lt(180 * m - 90)
        fd(x)
    #迭代
    else:
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
    setposition(-300,-150)      #图片起始位置
    pendown()

#初始化
title('希尔波特曲线')             #标题
speed(0)                        #速度
pic_resolution = 5              #分辨率对应阶数(增大此值可提高分辨率,但是速度极慢)
maxx = 320                      #最大步长
x = 320 / (2 ** pic_resolution) # 步长
hideturtle()                    #隐藏指针
colormode(255)                  #255rgb
pensize(x*1.3)
screensize(800, 500, "white")
setup(width=800, height=500)

#画标题
penup()
setposition(40,115)
write('What Is This?',font=("Arial",50,"normal"))
home()
pendown()


#画希尔伯特曲线
init()
hilbert_curve(pic_resolution, 0)
penup()
setposition(40,15)
pendown()
color('black')
write(name + '!',font=("Arial",50,"normal"))
exitonclick()
