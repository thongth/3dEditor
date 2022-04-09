import sys

from PySide2.QtWidgets import (QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QWidget, QPushButton)
from object3d.ThreeDObject import ThreeDObject

from view import (ThreeDViewer, ObjectListPanel, ObjectInfoPanelBox, ObjectInfoPanelSphere)
from object3d import (Sphere, Box)
from util.LocalStorage import JsonLocalStorage

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.objects = []
        self.selectedObject = None
        self.maxObjectNumber = 0

        self.renderWindow()
        self.loadData()

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
        
        self.threeDViewer.setRootEntity(self.rootEntity)

    def onObjectNameChange(self, newName: str):
        self.objectListPanel.updateList(self.objects)
        self.objectListPanel.selectItem(newName)

    def updateListPanel(self):
        self.objectListPanel.updateList(self.objects)

    def addSphere(self, name:str=None, loadMode:bool=False):
        if name == None: 
            name = 'sphere' + str(self.maxObjectNumber)
            self.maxObjectNumber += 1
        sphere = Sphere(self.rootEntity, name, self.onObjectNameChange, loadMode, self.saveData, self.setSelectedObject)
        self.updateMeshOnScreen(sphere, loadMode)

    def addBox(self, name:str=None, loadMode:bool=False):
        if name == None: 
            name = 'box' + str(self.maxObjectNumber)
            self.maxObjectNumber += 1
        box = Box(self.rootEntity, name, self.onObjectNameChange, loadMode, self.saveData, self.setSelectedObject)
        self.updateMeshOnScreen(box, loadMode)

    def updateMeshOnScreen(self, mesh: ThreeDObject, loadMode: bool=False):
        self.objects.append(mesh)
        self.updateListPanel()
        if not loadMode: self.saveData()

    def removeObject(self):
        toRemove = self.getSelectedObjectIndex()
        if toRemove != -1:
            self.objects[toRemove].setParent(None)
            self.objects.pop(toRemove)
            self.selectObject(None)
            self.objectListPanel.updateList(self.objects)
        self.saveData()
        print('pop', toRemove)

    def setSelectedObject(self, selectedObject: str):
        self.objectListPanel.selectItem(selectedObject)
        self.selectObject(selectedObject)

    def selectObject(self, selectedObject: str):
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

    def findIndexFromObjectName(self, name:str):
        for index, object in enumerate(self.objects):
            if object and name == object.name:
                return index
        return -1

    def saveData(self):
        data = {}
        objectList = []
        data['maxObjectNumber'] = self.maxObjectNumber
        for o in self.objects:
            objectData = {}
            objectData['name'] = o.name
            objectData['orientation'] = o.getOrientation()
            objectData['translation'] = [o.getTranslation().x(), o.getTranslation().y(), o.getTranslation().z()]
            objectData['color'] = o.getColor()
            if isinstance(o, Box):
                objectData['type'] = 'BOX'
                objectData['size'] = o.getSize()
            elif isinstance(o, Sphere):
                objectData['type'] = 'SPHERE'
                objectData['size'] = o.getRadius()
            objectList.append(objectData)
        data['objects'] = objectList
        JsonLocalStorage.saveLatest(data)

    def loadData(self):
        data = JsonLocalStorage.loadLatest()
        if data:
            self.maxObjectNumber = data['maxObjectNumber']
            for o in data['objects']:
                if o['type'] == "BOX":
                    self.addBox(o['name'], True)
                    self.objects[-1].setWidth(o['size'][0])
                    self.objects[-1].setHeight(o['size'][1])
                    self.objects[-1].setDepth(o['size'][2])
                else:
                    self.addSphere(o['name'], True)
                    self.objects[-1].setRadius(o['size'])
                self.objects[-1].updateName(o['name'])
                self.objects[-1].setTranslation(o['translation'][0], o['translation'][1], o['translation'][2])
                self.objects[-1].setOrientation(o['orientation'][2], o['orientation'][0], o['orientation'][1])
                self.objects[-1].setColor(o['color'][0], o['color'][1], o['color'][2])
        self.selectedObject = None

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.resize(1500, 800)
    w.show()
    app.exec_()
