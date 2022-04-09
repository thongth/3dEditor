import random

from PySide2.QtGui import (QVector3D, QColor, QQuaternion, qRgb)
from PySide2.Qt3DExtras import (Qt3DExtras)
from PySide2.Qt3DCore import (Qt3DCore)
from PySide2.Qt3DRender import (Qt3DRender)

class ThreeDObject():
    def __init__(self, name, rootEntity, onNameChange=None, nonRandom=False, onSave=None, onSelect=None):
        self.name = name
        self.onNameChange = onNameChange
        self.onSave = onSave
        self.onSelect = onSelect
        self.rootEntity = rootEntity

        self.entity = Qt3DCore.QEntity(self.rootEntity)
        
        self.material = Qt3DExtras.QPhongMaterial(self.rootEntity)
        self.material.setDiffuse(QColor(qRgb(102,224,255)))

        # Picker
        self.picker = Qt3DRender.QObjectPicker(self.rootEntity)
        self.picker.setDragEnabled(True)
        self.picker.clicked.connect(self.onPickerClick)
        self.picker.moved.connect(self.onPickerMove)

        self.transform = Qt3DCore.QTransform()
        self.entity.addComponent(self.transform)
        if not nonRandom:
            self.transform.setTranslation(QVector3D(random.random()*10, random.random()*10, 1))

        self.entity.addComponent(self.material)
        self.entity.addComponent(self.picker)

    def setPosition(self, x: float, y: float, z: float):
        self.transform.setTranslation(QVector3D(x, y, z))

    def setParent(self, parent=None):
        self.entity.setParent(parent)

    def updateName(self, name: str):
        self.name = name
        if self.onNameChange != None: 
            self.onNameChange(name)
            self.saveValue()

    def getTranslation(self):
        return self.transform.translation()

    def setTranslation(self, x: float, y: float, z: float):
        self.transform.setTranslation(QVector3D(x, y, z))
        self.saveValue()

    def getOrientation(self):
        return [self.transform.rotationX(), self.transform.rotationY(), self.transform.rotationZ()]

    def setOrientation(self, r: float, p: float, y: float):
        self.transform.setRotation(QQuaternion.fromEulerAngles(p, y, r))
        self.saveValue()

    def getColor(self):
        return self.material.diffuse().getRgb()

    def setColor(self, r: int, g: int, b: int):
        self.material.setDiffuse(QColor(qRgb(r, g, b)))
        self.saveValue()

    def saveValue(self):
        if self.onSave != None: self.onSave()
    
    def onPickerClick(self, p):
        if self.onSelect != None: self.onSelect(self.name)

    def onPickerMove(self, p):
        self.setTranslation(p.worldIntersection().x(), p.worldIntersection().y(), p.worldIntersection().z())

    def __str__(self):
        return self.name