'''
用turtle和希尔伯特曲线画出一个8*8点阵的icon
代表游戏我的世界中一个角色"Creeper"
'''
from turtle import *

def hilbert_curve(n, m):#用迭代绘制希尔伯特曲线
    index=1
    if n == 1:                  #出栈条件
        pos = position()
        fd(x)
        lt(180 * m - 90)
        fd(x)
        lt(180 * m - 90)
        fd(x)
        color()


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


#初始化
title('希尔波特曲线')     #标题
speed(0)                #速度
pic_resolution = 5      #分辨率对应阶数
x = 10                  #步长
hideturtle()            #隐藏指针
colormode(255)          #255rgb
pensize(10)

screensize(900, 600, "white")
setup(width=900, height=600)

penup()
setposition(-400,200)
write('creeper',font=("Arial",100,"normal"))
home()
pendown()


#画图初始化
def init():
    penup()
    setposition(-200,-200)
    pendown()
    lt(90)
    pendown()

init()
hilbert_curve(pic_resolution, 0)
get_shapepoly()
exitonclick()