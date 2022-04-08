import random

from PySide2.QtGui import (QVector3D, QColor, qRgb)
from PySide2.Qt3DCore import (Qt3DCore)
from PySide2.Qt3DExtras import (Qt3DExtras)

from .ThreeDObject import (ThreeDObject)

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
