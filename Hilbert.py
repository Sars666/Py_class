'''
运用所学的编程知识，基于海龟库独立完成一幅作品，并使得它动起来。√
• 要求包含函数定义、分支和循环语句√
• 代码中包含充分的注释和说明√
• 利用markdown格式写代码的说明文档√
• (可选)上传到github等服务器√
• 根据工作量和创意进行评分
'''

from turtle import *
from random import randint

def setrandomcolor():           #随机颜色/用radint设置255rgb模式
    colormode(255)              #浅色看不见
    color(randint(33,255),randint(33,255),randint(33,255))


def hb_curve(n,m):                      #m=0顺时针;m=1逆时针;
    if n == 1:                          #原点开始左上到右下,
                                        # 第一步不用转角,易于迭代2-1-4-3象限走
       fd(x)
       lt(180 * m - 90)
       fd(x)
       lt(180 * m - 90)
       fd(x)
    else:
        lt(180 * m - 90)#观察得希尔伯特曲线每增加一阶,始端和终端都顺时针翻转90°;
        hb_curve(n - 1,1 - m)#且顺时针逆时针互换,则翻转角每次改变180°,m→(1-m)[零一互换]
        lt(180 * m - 90)
        fd(x)
        hb_curve(n - 1,m)
        lt(180 * m + 90)
        fd(x)
        lt(180 * m + 90)
        hb_curve(n - 1,m)
        fd(x)
        lt(180 * m - 90)
        hb_curve(n - 1,1 - m)
        lt(180 * m - 90)
        setrandomcolor()
#初始化
title('希尔波特曲线') #标题
speed(0)          #速度
max = 10            #最大阶数
x = 600               #步长
hideturtle()        #隐藏乌龟


def reset():                    #重新设置乌龟的位置,并清除之前的图
    penup()
    setposition(-300,-300)
    setheading(0)
    clear()


def init(n):
    lt(90)                      #设置左下到右下,以便于二维转一维(左右拉伸)
    pendown()

for n in range(1,max+1):        #从1阶到max阶
    x = x/2
    reset()
    init(n)
    hb_curve(n,0)

exitonclick()