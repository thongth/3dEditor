import sys

from PySide2.QtWidgets import (QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QWidget, QPushButton)

from view import (ThreeDViewer, ObjectListPanel, ObjectInfoPanelBox, ObjectInfoPanelSphere)
from object3d import (Sphere, Box)

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
        self.container = QWidget.createWindowContainer(self.threeDViewer)
        self.container.setMinimumSize(1200, 800)
        self.rootEntity = self.threeDViewer.rootEntity

        appLayout = QHBoxLayout()
        configLayout = QVBoxLayout()
        buttonBar = QHBoxLayout()

        self.newSphereButton = QPushButton('New Sphere')
        self.newSphereButton.clicked.connect(self.addSphere)
        self.newBoxButton = QPushButton('New Box')
        self.newBoxButton.clicked.connect(self.addBox)
        self.removeObjectButton = QPushButton('Remove Object')
        self.removeObjectButton.clicked.connect(self.removeObject)

        self.objectListPanel = ObjectListPanel(self.selectObject)
        self.objectInfoPanelBox = ObjectInfoPanelBox()
        self.objectInfoPanelSphere = ObjectInfoPanelSphere()
        self.objectInfoPanelBox.setVisible(False)
        self.objectInfoPanelSphere.setVisible(False)

        buttonBar.addWidget(self.newSphereButton)
        buttonBar.addWidget(self.newBoxButton)
        buttonBar.addWidget(self.removeObjectButton)

        configLayout.addLayout(buttonBar)
        configLayout.addWidget(self.objectListPanel)
        configLayout.addWidget(self.objectInfoPanelBox)
        configLayout.addWidget(self.objectInfoPanelSphere)

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

    def addSphere(self):
        sphere = Sphere(self.rootEntity, 'sphere' + str(self.maxObjectNumber), self.onObjectNameChange)
        self.updateMeshOnScreen(sphere)

    def addBox(self):
        box = Box(self.rootEntity, 'box' + str(self.maxObjectNumber), self.onObjectNameChange)
        self.updateMeshOnScreen(box)

    def updateMeshOnScreen(self, mesh):
        self.objects.append(mesh)
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
        self.setObjectInfoPanel()

    def setObjectInfoPanel(self):
        object = self.getSelectedObject()
        if isinstance(object, Box):
            self.objectInfoPanelBox.setSelectedObject(self.getSelectedObject())
        else:
            self.objectInfoPanelSphere.setSelectedObject(self.getSelectedObject())
        self.setVisibilityBasedOnSelectedObject()

    def setVisibilityBasedOnSelectedObject(self):
        object = self.getSelectedObject()
        boxVisibility = isinstance(object, Box)
        sphereVisibility = isinstance(object, Sphere)
        if self.objectInfoPanelBox.isVisible() != boxVisibility:
            print('0')
            self.objectInfoPanelBox.setVisible(isinstance(object, Box))
            self.objectInfoPanelBox.focusNameInput()
        if self.objectInfoPanelSphere.isVisible() != sphereVisibility:
            print('1')
            self.objectInfoPanelSphere.setVisible(isinstance(object, Sphere))
            self.objectInfoPanelSphere.focusNameInput()

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
