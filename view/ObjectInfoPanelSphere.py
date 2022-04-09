from PySide2.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QLabel, QLineEdit, QSlider
from PySide2.QtCore import Qt

from object3d.Sphere import Sphere

from .ObjectInfoPanel import ObjectInfoPanel

class ObjectInfoPanelSphere(ObjectInfoPanel):
    def __init__(self, parent=None):
        super(ObjectInfoPanelSphere, self).__init__(parent)

        # Radius
        self.radiusLayout = QHBoxLayout()
        self.radiusLabel = QLabel("Radius")
        self.radiusInput = QSlider(Qt.Horizontal)
        self.radiusInput.setMinimum(1)
        self.radiusInput.setMaximum(10)
        self.radiusInput.sliderMoved.connect(self.onRadiusChange)
        self.radiusLayout.addWidget(self.radiusLabel)
        self.radiusLayout.addWidget(self.radiusInput)

        self.layout.addLayout(self.radiusLayout)

        self.setLayout(self.layout)

    def onRadiusChange(self, r):
        self.selectedObject.setRadius(r)

    def setOther(self, object):
        if isinstance(object, Sphere):
            self.radiusInput.setValue(int(object.getRadius()))