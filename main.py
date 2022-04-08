from email.charset import QP
import sys
import random

from PySide2.QtWidgets import (QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QWidget, QPushButton)
from PySide2.QtCore import(Property, QObject, QPropertyAnimation, Signal)
from PySide2.QtGui import (QMatrix4x4, QQuaternion, QVector3D, QColor, qRgb)
from PySide2.Qt3DCore import (Qt3DCore)
from PySide2.Qt3DExtras import (Qt3DExtras)

from view import ThreeDViewer, ObjectListPanel, ObjectInfoPanel
from object3d import Sphere
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.objects = []
        self.selectedObject = None
        self.maxObjectNumber = 0

        self.renderWindow()

    def renderWindow(self):
        self.setWindowTitle("3d Editor")

        self.threeDViewer = ThreeDViewer()
        self.threeDViewer.defaultFrameGraph().setClearColor(QColor(qRgb(255,221,153)))
        self.container = QWidget.createWindowContainer(self.threeDViewer)
        self.container.setMinimumSize(1200, 800)
        self.rootEntity = self.threeDViewer.rootEntity

        appLayout = QHBoxLayout()
        configLayout = QVBoxLayout()
        buttonBar = QHBoxLayout()

        self.newObjectButton = QPushButton('New Object')
        self.newObjectButton.clicked.connect(self.addSphere)
        self.removeObjectButton = QPushButton('Remove Object')
        self.removeObjectButton.clicked.connect(self.removeObject)

        self.objectListPanel = ObjectListPanel(self.selectObject)
        self.objectInfoPanel = ObjectInfoPanel()

        buttonBar.addWidget(self.newObjectButton)
        buttonBar.addWidget(self.removeObjectButton)

        configLayout.addLayout(buttonBar)
        configLayout.addWidget(self.objectListPanel)
        configLayout.addWidget(self.objectInfoPanel)

        appLayout.addWidget(self.container)
        appLayout.addLayout(configLayout)

        widget = QWidget()
        widget.setLayout(appLayout)
        self.setCentralWidget(widget)
        
        self.addSphere()
        self.addSphere()
        self.threeDViewer.setRootEntity(self.rootEntity)

    def onObjectNameChange(self, newName):
        self.objectListPanel.updateList(self.objects)
        self.objectListPanel.selectItem(newName)

    def updateListPanel(self):
        self.objectListPanel.updateList(self.objects)

    def addSphere(self, radius=3):
        sphere = Sphere(self.rootEntity, 'sphere' + str(self.maxObjectNumber), radius, self.onObjectNameChange)
        self.objects.append(sphere)
        self.updateListPanel()
        self.maxObjectNumber += 1

    def removeObject(self):
        toRemove = self.getSelectedObjectIndex()
        if toRemove != -1:
            self.objects[toRemove].setParent(None)
            self.objects.pop(toRemove)
            self.selectObject(None)
            self.objectListPanel.updateList(self.objects)
        print('pop', toRemove)

    def selectObject(self, selectedObject):
        print(selectedObject)
        self.selectedObject = selectedObject
        self.objectInfoPanel.setSelectedObject(self.getSelectedObject())

    def getSelectedObject(self):
        index = self.getSelectedObjectIndex()
        if index == -1: return None
        return self.objects[index]

    def getSelectedObjectIndex(self):
        return self.findIndexFromObjectName(self.selectedObject)

    def findIndexFromObjectName(self, name):
        for index, object in enumerate(self.objects):
            if object and name == object.name:
                return index
        return -1

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.resize(1500, 800)
    w.show()
    app.exec_()
