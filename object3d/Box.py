from PySide2.Qt3DExtras import (Qt3DExtras)

from .ThreeDObject import (ThreeDObject)

class Box(ThreeDObject):
    def __init__(self, rootEntity, name, radius, onNameChange=None):
        super().__init__(name, rootEntity, onNameChange)
        self.radius = radius
        self._createBox()

    def _createBox(self):
        self.boxMesh = Qt3DExtras.QCuboidMesh()

        self.entity.addComponent(self.boxMesh)