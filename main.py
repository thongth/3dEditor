from PySide2.QtWidgets import (QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QWidget, QListWidget)
from PySide2.QtCore import(Property, QObject, QPropertyAnimation, Signal)
from PySide2.QtGui import (QMatrix4x4, QQuaternion, QVector3D, QColor, qRgb)

from PySide2.Qt3DCore import (Qt3DCore)
from PySide2.Qt3DExtras import (Qt3DExtras)

import sys
import random

class ThreeDObject():
    def __init__(self, name, rootEntity):
        self.name = name
        self.rootEntity = rootEntity

    def updateName(self, name):
        self.name = name

class ThreeDViewer(Qt3DExtras.Qt3DWindow):
    def __init__(self, parent=None):
        super(ThreeDViewer, self).__init__(parent)
        self.rootEntity = Qt3DCore.QEntity()

        # Camera
        self.camera().lens().setPerspectiveProjection(45, 16 / 9, 0.1, 1000)
        self.camera().setPosition(QVector3D(0, 0, 40))
        self.camera().setViewCenter(QVector3D(0, 0, 0))

        # Camera Control
        self.camController = Qt3DExtras.QOrbitCameraController(self.rootEntity)
        self.camController.setLinearSpeed(50)
        self.camController.setLookSpeed(180)
        self.camController.setCamera(self.camera())
        self.setRootEntity(self.rootEntity)


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

class ObjectInfoPanel(QWidget):
    def __init__(self, parent=None):
        super(ObjectInfoPanel, self).__init__(parent)
        

class ObjectListModel():
    def __init__(self):
        self.objects = []

    def addBox(self):
        self.objects.append()

class Sphere(ThreeDObject):
    def __init__(self, rootEntity, name, radius):
        super().__init__(name, rootEntity)
        self.radius = radius
        self._createSphere()

    def _createSphere(self):
        self.rootEntity = self.rootEntity
        self.sphereEntity = Qt3DCore.QEntity(self.rootEntity)
        self.sphereMesh = Qt3DExtras.QSphereMesh()
        self.sphereMesh.setRadius(self.radius)

        self.material = Qt3DExtras.QPhongMaterial(self.rootEntity)
        self.material.setDiffuse(QColor(qRgb(102,224,255)))

        self.sphereTransform = Qt3DCore.QTransform()
        self.sphereEntity.addComponent(self.sphereTransform)
        self.sphereTransform.setTranslation(QVector3D(1.5, random.random()*10, 1))

        self.sphereEntity.addComponent(self.sphereMesh)
        self.sphereEntity.addComponent(self.material)

    def setPosition(self, x, y, z):
        self.sphereTransform.setTranslation(QVector3D(x, y, z))

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("3d Editor")

        self.threeDViewer = ThreeDViewer()
        self.threeDViewer.defaultFrameGraph().setClearColor(QColor(qRgb(255,221,153)))
        self.container = QWidget.createWindowContainer(self.threeDViewer)
        self.container.setMinimumSize(1200, 800)
        self.rootEntity = self.threeDViewer.rootEntity

        self.objects = []

        appLayout = QHBoxLayout()
        configLayout = QVBoxLayout()

        self.objectListPanel = ObjectListPanel()
        self.objectInfoPanel = ObjectInfoPanel()

        configLayout.addWidget(self.objectListPanel)
        configLayout.addWidget(self.objectInfoPanel)

        appLayout.addWidget(self.container)
        appLayout.addLayout(configLayout)

        widget = QWidget()
        widget.setLayout(appLayout)
        self.setCentralWidget(widget)
        
        sphere = Sphere(self.rootEntity, 'sphere1', 3)
        self.objects.append(sphere)
        self.objectListPanel.updateList(self.objects)

        self.threeDViewer.setRootEntity(self.rootEntity)

    # def addSphere(self):
    #     self.sphereEntity = Qt3DCore.QEntity(self.rootEntity)
    #     self.sphereMesh = Qt3DExtras.QSphereMesh()
    #     self.sphereMesh.setRadius(3)

    #     self.material = Qt3DExtras.QPhongMaterial(self.rootEntity)

    #     self.sphereTransform = Qt3DCore.QTransform()

    #     self.sphereEntity.addComponent(self.sphereMesh)
    #     self.sphereEntity.addComponent(self.sphereTransform)
    #     self.sphereEntity.addComponent(self.material)

        # self.objects.append(sphereEntity)


app = QApplication(sys.argv)
w = MainWindow()
w.resize(1500, 800)
w.show()
app.exec_()
