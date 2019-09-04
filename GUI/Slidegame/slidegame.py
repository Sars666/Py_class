# 游戏说明：把'心'图案放在第一个记为胜利

import random
import sys
from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


# 定义BlockWindow窗口类
class ElementWigets(QWidget):
    def __init__(self):
        super().__init__()
        # 固定窗口
        self.setFixedSize(sideLength * 3, sideLength * 3)

        # 生成label对象
        self.label = []
        for i in range(0, 9, 1):
            self.label0 = QtWidgets.QLabel(self)
            self.label.append(self.label0)
        # Qlabel对象初始化
        for i in range(3):
            for j in range(3):
                ix = i * 3 + j
                x = sideLength * j + spacing
                y = sideLength * i + spacing
                self.label[ix].setGeometry(QtCore.QRect(x, y,
                                                        sideLength - 2 * spacing, sideLength - 2 * spacing))
                # 显示图片
                png = QtGui.QPixmap(str(ix) + '.png')
                self.label[ix].setPixmap(png)


class ViewController(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.setWindowTitle("slideGame")

    # 初始化UI界面
    def initUI(self):

        vLayout = QVBoxLayout()  # 垂直布局

        self.canvas = ElementWigets()
        self.shuffleButton = QPushButton('Shuffle', self)

        self.shuffleButton.clicked.connect(self.onShuffle)

        # 垂直布局
        vLayout.addWidget(self.canvas, alignment=Qt.AlignCenter)
        vLayout.addWidget(self.shuffleButton)
        self.setFixedSize(sideLength * 4, sideLength * 4)
        self.center()
        self.setLayout(vLayout)

    def getNum(self, i, j):
        if 0 <= i < 3 and 0 <= j < 3:
            ix = i * 3 + j
            return idList[ix]
        else:
            return -1

    # 交换(a,b)(从,d)
    def swap(self, a, b, c, d):
        ix1 = a * 3 + b
        ix2 = c * 3 + d
        idList[ix1], idList[ix2] = idList[ix2], idList[ix1]
        self.update()

    # 重定义鼠标按下事件
    def mousePressEvent(self, evt):

        x, y = evt.x(), evt.y()  # 取得鼠标当前坐标
        j = int(x / sideLength)  # 取整
        i = int(y / sideLength)

        # 判断鼠标是否点到空白并交换
        if 0 <= i < 3 and 0 <= j < 3:
            if self.getNum(i - 1, j) == 0:
                self.swap(i, j, i - 1, j)
            elif self.getNum(i + 1, j) == 0:
                self.swap(i, j, i + 1, j)
            elif self.getNum(i, j - 1) == 0:
                self.swap(i, j, i, j - 1)
            elif self.getNum(i, j + 1) == 0:
                self.swap(i, j, i, j + 1)

        # 刷新布局
        for ix in range(0, 9, 1):
            png = QtGui.QPixmap(str(idList[ix]) + '.png')
            self.canvas.label[ix].setPixmap(png)
            QApplication.processEvents()  # 更新界面

        # 胜利条件判断
        if self.gameFinished():
            QMessageBox.question(self, 'Congratulation',
                                 'You DID it!', QMessageBox.Ok)
            exit()

    # 当'心'到第一位即判断胜利
    def gameFinished(self):
        if idList[0] == 1:
            return 1
        else:
            return 0

    # 随机打乱函数
    def onShuffle(self, evt):
        random.shuffle(idList)
        for ix in range(0, 9, 1):
            png = QtGui.QPixmap(str(idList[ix]) + '.png')
            self.canvas.label[ix].setPixmap(png)
            QApplication.processEvents()  # 更新界面

    # 游戏居中
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


# 初始化数据
spacing = 1
sideLength = 100

# id数组,用来进行数据操作
idList = list(range(9))

# 图像数组，用来存储对应的图像
imgs = []
img0 = Image.new('RGB', (sideLength - 2 * spacing, sideLength - 2 * spacing), (236, 236, 236))
img0.save('0.png')
for i in range(0, 9, 1):
    img0 = Image.open(str(i) + '.png')
    img = img0.resize((sideLength - 2 * spacing, sideLength - 2 * spacing), Image.NEAREST)
    img.save(str(i) + '.png')
    imgs.append(img)

app = QApplication(sys.argv)
View = ViewController()
View.show()
sys.exit(app.exec_())
