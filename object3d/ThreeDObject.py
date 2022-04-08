import random

from PySide2.QtGui import (QVector3D, QColor, qRgb)
from PySide2.Qt3DExtras import (Qt3DExtras)
from PySide2.Qt3DCore import (Qt3DCore)

class ThreeDObject():
    def __init__(self, name, rootEntity, onNameChange=None):
        self.name = name
        self.onNameChange = onNameChange
        self.rootEntity = rootEntity

        self.entity = Qt3DCore.QEntity(self.rootEntity)
        
        self.material = Qt3DExtras.QPhongMaterial(self.rootEntity)
        self.material.setDiffuse(QColor(qRgb(102,224,255)))

        self.transform = Qt3DCore.QTransform()
        self.entity.addComponent(self.transform)
        self.transform.setTranslation(QVector3D(random.random()*10, random.random()*10, 1))

        self.entity.addComponent(self.material)

    def setPosition(self, x, y, z):
        self.transform.setTranslation(QVector3D(x, y, z))

    def setParent(self, parent=None):
        self.entity.setParent(parent)

    def updateName(self, name):
        self.name = name
        if self.onNameChange != None: self.onNameChange(name)

    def __str__(self):
        return self.name