
from PySide2.QtWidgets import (QHBoxLayout, QWidget, QListWidget)
from PySide2.QtCore import Qt

from object3d.ThreeDObject import ThreeDObject

class ObjectListPanel(QWidget):
    def __init__ (self, onObjectSelected, parent=None):
        super(ObjectListPanel, self).__init__(parent)

        self.objectList = QListWidget()
        self.objectList.currentTextChanged.connect(onObjectSelected)

        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.addWidget(self.objectList)
        self.setLayout(layout)

    def updateList(self, objects: list[ThreeDObject]):
        self.objectList.clear()
        self.objectList.addItems([s.name for s in objects])

    def selectItem(self, text: str):
        toSelectItem = self.findItemByText(text)
        print('toSelectItem', toSelectItem)
        if toSelectItem != None:
            self.objectList.setCurrentItem(toSelectItem[0])

    def findItemByText(self, text: str):
        print(text)
        return self.objectList.findItems(text, Qt.MatchExactly)