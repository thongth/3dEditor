from PySide2.QtWidgets import QHBoxLayout, QLabel, QSlider
from PySide2.QtCore import Qt

from object3d.Box import Box

from .ObjectInfoPanel import ObjectInfoPanel

class ObjectInfoPanelBox(ObjectInfoPanel):
    def __init__(self, parent=None):
        super(ObjectInfoPanelBox, self).__init__(parent)

        # Width
        self.widthLayout = QHBoxLayout()
        self.widthLabel = QLabel("Width")
        self.widthInput = QSlider(Qt.Horizontal)
        self.widthInput.setMinimum(1)
        self.widthInput.setMaximum(10)
        self.widthInput.sliderMoved.connect(self.onWidthChange)
        self.widthLayout.addWidget(self.widthLabel)
        self.widthLayout.addWidget(self.widthInput)

        # Height
        self.heightLayout = QHBoxLayout()
        self.heightLabel = QLabel("Height")
        self.heightInput = QSlider(Qt.Horizontal)
        self.heightInput.setMinimum(1)
        self.heightInput.setMaximum(10)
        self.heightInput.sliderMoved.connect(self.onHeightChange)
        self.heightLayout.addWidget(self.heightLabel)
        self.heightLayout.addWidget(self.heightInput)

        # Depth
        self.depthLayout = QHBoxLayout()
        self.depthLabel = QLabel("Depth")
        self.depthInput = QSlider(Qt.Horizontal)
        self.depthInput.setMinimum(1)
        self.depthInput.setMaximum(10)
        self.depthInput.sliderMoved.connect(self.onDepthChange)
        self.depthLayout.addWidget(self.depthLabel)
        self.depthLayout.addWidget(self.depthInput)

        self.layout.addLayout(self.widthLayout)
        self.layout.addLayout(self.heightLayout)
        self.layout.addLayout(self.depthLayout)

        self.setLayout(self.layout)

    def onWidthChange(self, w):
        self.selectedObject.setWidth(w)
        
    def onHeightChange(self, h):
        self.selectedObject.setHeight(h)
        
    def onDepthChange(self, d):
        self.selectedObject.setDepth(d)

    def setOther(self, object):
        if isinstance(object, Box):
            (x, y, z) = object.getSize()
            self.widthInput.setValue(int(x))
            self.heightInput.setValue(int(y))
            self.depthInput.setValue(int(z))