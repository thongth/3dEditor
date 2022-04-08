from PySide2.Qt3DExtras import (Qt3DExtras)

from .ThreeDObject import (ThreeDObject)

class Sphere(ThreeDObject):
    def __init__(self, rootEntity, name, radius):
        super().__init__(name, rootEntity)
        self.radius = radius
        self._createSphere()

    def _createSphere(self):
        self.sphereMesh = Qt3DExtras.QSphereMesh()

        self.entity.addComponent(self.sphereMesh)
