import sys
import random

from PySide2.QtWidgets import (QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QWidget, QListWidget)
from PySide2.QtCore import(Property, QObject, QPropertyAnimation, Signal)
from PySide2.QtGui import (QMatrix4x4, QQuaternion, QVector3D, QColor, qRgb)
from PySide2.Qt3DCore import (Qt3DCore)
from PySide2.Qt3DExtras import (Qt3DExtras)

from view import ThreeDViewer, ObjectListPanel, ObjectInfoPanel
from object3d import Sphere
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.resize(1500, 800)
    w.show()
    app.exec_()
