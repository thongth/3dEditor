from PySide2.Qt3DCore import (Qt3DCore)
from PySide2.Qt3DExtras import (Qt3DExtras)
from PySide2.QtGui import (QVector3D, QColor, qRgb)
from PySide2.Qt3DRender import (Qt3DRender)

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

        # Light
        self.lightEntity = Qt3DCore.QEntity(self.rootEntity)
        self.light = Qt3DRender.QPointLight(self.lightEntity)
        self.light.setColor('white')
        self.light.setIntensity(1)
        self.lightEntity.addComponent(self.light)
        self.lightTransform = Qt3DCore.QTransform(self.lightEntity)
        self.lightTransform.setTranslation(self.camera().position())
        self.lightEntity.addComponent(self.lightTransform)

        # Background
        self.defaultFrameGraph().setClearColor(QColor(qRgb(255,221,153)))