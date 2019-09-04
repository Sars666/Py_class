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
        self.ElementDic = {'1': 'Element_fire.png',
                           '2': 'Element_water.png',
                           '3': 'Element_earth.png',
                           '4': 'Element_life.png',
                           '5': 'Element_arcane.png',
                           '6': 'Element_shield.png'}
        rows = 5
        columns = 6
        self.elementList = []

        self.setAcceptDrops(True)
        # 布局设置
        grid = QGridLayout()
        self.setLayout(grid)
        grid.setSpacing(0)

        elementImgIdList = self.initialElement(rows, columns)
        positions = [(r, c) for r in range(rows)
                     for c in range(columns)]
        self.drawElement(positions, elementImgIdList, grid)

    def drawElement(self, positions, elementImgIdList, grid):
        elementId = 1
        for position, elementImgId in zip(positions, elementImgIdList):
            if elementImgId == '':
                continue
            element = Button('', self, elementImgId, self.ElementDic)
            element.elementId = elementId
            elementId += 1
            element.setFixedSize(50, 50)
            self.elementList.append(element)
            grid.addWidget(element, *position)

    def initialElement(self, rows, columns):
        elementImgIdList = []
        for r in range(rows):
            for c in range(columns):
                elementImgIdList.append(str(random.randint(1, 6)))
        return elementImgIdList

    def dragEnterEvent(self, e):
        e.accept()
        self.pressBtnPos = e.pos()#drag时的位置作为要操作的btn的位置
        print(self.pressBtnPos)


    def dropEvent(self, e):
        position = self.pressBtnPos
        elementPosId = self.position2Id(position)
        print(elementPosId)
        try:
            newPos =self.getRigidPos(QPoint(e.pos().x() - 20, e.pos().y() - 20))
            self.elementList[elementPosId].move(newPos)

        except IndexError:
            pass
        e.setDropAction(Qt.MoveAction)
        e.accept()
        self.swapElement(self.elementList,elementPosId,self.position2Id(newPos))

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
        return posId

    def updateId(self):
        pass

    def swapElement(self, elementIdList, element_1, element_2):
        elementIdList[element_1], elementIdList[element_2] = \
            elementIdList[element_2], elementIdList[element_1]

    def match(self):
        pass

    def eliminateMatchedElement(self):
        pass

    def generateNewElement(self):
        pass

    def blockFall(self):
        pass

    def updateBtnPos(self,btn,pos):
        pos = self.getMouthPos()
        btn.setPos(pos)

    def getMousePos(self):
        x, y = pag.position()  # 返回鼠标的坐标
        print(x,y)
        rect = self.window().frameGeometry()
        x = x - rect.top()
        y = y - rect.left()
        posStr = x, y
        time.sleep(0.01)
        print(posStr)
        return QPoint(x,y)

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

    def mouseMoveEvent(self, e):
        if e.buttons() != Qt.LeftButton:
            return
        mimeData = QMimeData()
        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(QPoint(0, 0))
        row = int(self.elementId / 6)
        if row < 1: row = 1
        dropAction = drag.exec_(Qt.MoveAction)

    def mousePressEvent(self, e):
        QPushButton.mousePressEvent(self, e)
        self.pressPosition = e.pos()
        self.isPressed = not self.isPressed
        if e.button() == Qt.LeftButton:
            print(self.elementId)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Element()
    ex.show()
    sys.exit(app.exec_())
