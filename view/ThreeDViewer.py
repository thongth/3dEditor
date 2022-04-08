from PySide2.Qt3DCore import (Qt3DCore)
from PySide2.Qt3DExtras import (Qt3DExtras)
from PySide2.QtGui import (QVector3D)

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