
import os,time
import pyautogui as pag
while True:
    x,y = pag.position() #返回鼠标的坐标
    posStr="Position:"+str(x).rjust(4)+','+str(y).rjust(4)
    print (posStr)#打印坐标
    time.sleep(0.01)
    os.system('cls')#清楚屏幕