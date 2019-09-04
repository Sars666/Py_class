# 游戏操作的元素块
import sys, random, time, os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import pyautogui as pag


class Element(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 基础信息
        self.id_1 = 0
        self.id_2 = 0
        self.elementList = []
        self.ElementDic = {'1': 'Element_fire.png',
                           '2': 'Element_water.png',
                           '3': 'Element_earth.png',
                           '4': 'Element_life.png',
                           '5': 'Element_arcane.png',
                           '6': 'Element_shield.png'}
        rows = 5
        columns = 6
        # 布局设置
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.grid.setSpacing(0)
        self.elementImgIdList = self.initialElement(rows, columns)
        self.positions = [(r, c) for r in range(rows) for c in range(columns)]
        self.drawElement(self.positions, self.elementImgIdList, self.grid)

    def initialElement(self, rows, columns):
        elementImgIdList = []
        for r in range(rows):
            for c in range(columns):
                elementImgIdList.append(str(random.randint(1, 6)))
        return elementImgIdList

    def drawElement(self, positions, elementImgIdList, grid):
        elementId = 1
        for position, elementImgId in zip(positions, elementImgIdList):
            if elementImgId == '':
                continue
            element = Button('', self, elementImgId, self.ElementDic)
            element.elementId = elementId
            elementId += 1
            element.setFixedSize(50, 50)
            element.clicked.connect(self.buttonClicked)
            self.elementList.append(element)
            grid.addWidget(element, *position)

    def mousePressEvent(self, QMouseEvent):
        self.reDrawElement(self.positions, self.elementImgIdList, self.grid)

    def buttonClicked(self):
        sender = self.sender()
        pressedElementNumber = self.pressedElementNumber(self.elementList)
        if pressedElementNumber%2 == 1:
            self.id_1 = (self.position2Id(sender.pos()))
        elif pressedElementNumber%2 == 0:
            self.id_2 = (self.position2Id(sender.pos()))
            self.swapElement(self.elementList, self.id_1, self.id_2)
            self.swapReset(self.elementList, self.id_1, self.id_2)
            self.drawElement(self.positions, self.elementImgIdList, self.grid)
        else:
            print('Error!')

    def swapElement(self, elementList, id_1, id_2):
        element_1 = elementList[id_1 - 1]
        element_2 = elementList[id_2 - 1]
        print(element_1, element_2)
        if element_1.isPressed == True and \
                        element_1.isPressed == True:
            element_1, element_2 = element_2, element_1
        print(element_1, element_2)

    def swapReset(self, elementList, id_1, id_2):
        elementList[id_1 - 1].isPressed = False
        elementList[id_2 - 1].isPressed = False

    def getRigidPos(self, position):
        x, y = position.x() / 50, position.y() / 50
        row, column = int(y), int(x)
        if row < 1: row = 0
        if row > 5: row = 5
        if column < 1: column = 0
        if column > 6: column = 6
        posY, posX = row * 50, column * 50
        pos = QPoint(posX + 20, posY + 20)
        return pos

    def position2Id(self, position):
        x, y = position.x() / 50, position.y() / 50
        row, column = int(y), int(x)
        if row < 1: row = 0
        if row > 5: row = 4
        if column < 1: column = 0
        if column > 6: column = 6
        posId = row * 6 + column
        return posId + 1

    def updateId(self):
        pass

    def match(self, elementList):
        for id in elementList:
            pass  # 判断是否match

    def eliminateMatchedElement(self, elementList, eliminateIdList):
        for eliminateId in elementList:
            elementList[eliminateId] = ''

    def pressedElementNumber(self, elementList):
        isPressedNumber = 0
        for id in range(len(elementList)):
            if elementList[id].isPressed:
                isPressedNumber += 1
        return isPressedNumber

    def generateNewElement(self):
        pass

    def blockFall(self):
        pass


class Button(QPushButton):
    def __init__(self, title, parent, elementId, ElementDic):
        super().__init__(title, parent)
        self.elementId = elementId
        self.ElementDic = ElementDic
        self.elementImgName = "ElementImg/" + self.ElementDic[self.elementId]
        styleSheet = 'QPushButton{border-image:url(' + self.elementImgName + ')}'
        self.setStyleSheet(styleSheet)
        self.isMatched = False
        self.isPressed = False

    def mousePressEvent(self, e):
        QPushButton.mousePressEvent(self, e)
        self.pressPosition = e.pos()
        self.isPressed = not self.isPressed
        if e.button() == Qt.LeftButton:
            print(self.elementId)
            print(self.isPressed)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Element()
    ex.show()
    sys.exit(app.exec_())
