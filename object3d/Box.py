from PySide2.Qt3DExtras import (Qt3DExtras)

from .ThreeDObject import (ThreeDObject)

class Box(ThreeDObject):
    def __init__(self, rootEntity, name, onNameChange=None):
        super().__init__(name, rootEntity, onNameChange)
        self._createBox()

    def _createBox(self):
        self.boxMesh = Qt3DExtras.QCuboidMesh()

        self.entity.addComponent(self.boxMesh)

    def getSize(self):
        return (self.boxMesh.xExtent(), self.boxMesh.yExtent(), self.boxMesh.zExtent())

    def setWidth(self, w):
        self.boxMesh.setXExtent(w)

    def setHeight(self, h):
        self.boxMesh.setYExtent(h)

    def setDepth(self, d):
        self.boxMesh.setZExtent(d)