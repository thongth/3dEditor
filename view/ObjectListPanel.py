
from PySide2.QtWidgets import (QHBoxLayout, QWidget, QListWidget)

class ObjectListPanel(QWidget):
    def __init__ (self, parent=None):
        super(ObjectListPanel, self).__init__(parent)

        self.objectList = QListWidget()
        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.addWidget(self.objectList)
        self.setLayout(layout)

    def updateList(self, objects):
        self.objectList.reset()
        self.objectList.addItems([s.name for s in objects])