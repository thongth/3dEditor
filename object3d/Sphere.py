from PySide2.Qt3DExtras import (Qt3DExtras)

from .ThreeDObject import (ThreeDObject)

class Sphere(ThreeDObject):
    def __init__(self, rootEntity, name, onNameChange=None, nonRandom=False, onSave=None, onSelect=None):
        super().__init__(name, rootEntity, onNameChange, nonRandom, onSave, onSelect)
        self._createSphere()

    def _createSphere(self):
        self.sphereMesh = Qt3DExtras.QSphereMesh()

        self.entity.addComponent(self.sphereMesh)

    def getRadius(self):
        return self.sphereMesh.radius()

    def setRadius(self, r: int):
        self.sphereMesh.setRadius(r)
        self.saveValue()