from PySide2.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QLabel, QLineEdit, QSlider
from PySide2.QtCore import Qt

from object3d.ThreeDObject import ThreeDObject

class ObjectInfoPanel(QWidget):
    def __init__(self, parent=None):
        super(ObjectInfoPanel, self).__init__(parent)
        self.selectedObject = None
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)

        # Name
        self.nameLayout = QHBoxLayout()
        self.nameLabel = QLabel("Name")
        self.nameInput = QLineEdit()
        self.nameInput.textEdited.connect(self.onNameChange)
        self.nameLayout.addWidget(self.nameLabel)
        self.nameLayout.addWidget(self.nameInput)

        # Translation
        self.translationLayout = QHBoxLayout()
        self.translationLabel = QLabel("Translation")
        self.translationInputX = QLineEdit()
        self.translationInputY = QLineEdit()
        self.translationInputZ = QLineEdit()
        self.translationInputX.textEdited.connect(self.onTranslationChange)
        self.translationInputY.textEdited.connect(self.onTranslationChange)
        self.translationInputZ.textEdited.connect(self.onTranslationChange)
        self.translationLayout.addWidget(self.translationLabel)
        self.translationLayout.addWidget(self.translationInputX)
        self.translationLayout.addWidget(self.translationInputY)
        self.translationLayout.addWidget(self.translationInputZ)

        # Orientation
        self.orientationLayout = QHBoxLayout()
        self.orientationLabel = QLabel("Orientation")
        self.orientationInputR = QLineEdit()
        self.orientationInputP = QLineEdit()
        self.orientationInputY = QLineEdit()
        self.orientationInputR.textEdited.connect(self.onOrientationChange)
        self.orientationInputP.textEdited.connect(self.onOrientationChange)
        self.orientationInputY.textEdited.connect(self.onOrientationChange)
        self.orientationLayout.addWidget(self.orientationLabel)
        self.orientationLayout.addWidget(self.orientationInputR)
        self.orientationLayout.addWidget(self.orientationInputP)
        self.orientationLayout.addWidget(self.orientationInputY)

        # Red color
        self.redLayout = QHBoxLayout()
        self.redLabel = QLabel("R")
        self.redInput = QSlider(Qt.Horizontal)
        self.redInput.setMinimum(1)
        self.redInput.setMaximum(255)
        self.redInput.sliderMoved.connect(self.onColorChange)
        self.redLayout.addWidget(self.redLabel)
        self.redLayout.addWidget(self.redInput)

        # Green color
        self.greenLayout = QHBoxLayout()
        self.greenLabel = QLabel("G")
        self.greenInput = QSlider(Qt.Horizontal)
        self.greenInput.setMinimum(1)
        self.greenInput.setMaximum(255)
        self.greenInput.sliderMoved.connect(self.onColorChange)
        self.greenLayout.addWidget(self.greenLabel)
        self.greenLayout.addWidget(self.greenInput)

        # Blue
        self.blueLayout = QHBoxLayout()
        self.blueLabel = QLabel("B")
        self.blueInput = QSlider(Qt.Horizontal)
        self.blueInput.setMinimum(1)
        self.blueInput.setMaximum(255)
        self.blueInput.sliderMoved.connect(self.onColorChange)
        self.blueLayout.addWidget(self.blueLabel)
        self.blueLayout.addWidget(self.blueInput)

        self.layout.addLayout(self.nameLayout)
        self.layout.addLayout(self.translationLayout)
        self.layout.addLayout(self.orientationLayout)
        self.layout.addLayout(self.redLayout)
        self.layout.addLayout(self.greenLayout)
        self.layout.addLayout(self.blueLayout)

        self.setLayout(self.layout)

        self.focusNameInput()

    def setSelectedObject(self, selectedObject: ThreeDObject):
        self.selectedObject = selectedObject
        self.setPlaceHolder(self.selectedObject)

    def setPlaceHolder(self, object: ThreeDObject):
        if object == None:
            self.setBlank()
            return

        # Set name
        self.nameInput.setText(object.name)

        # Set translation
        self.translationInputX.setText(str(object.getTranslation().x()))
        self.translationInputY.setText(str(object.getTranslation().y()))
        self.translationInputZ.setText(str(object.getTranslation().z()))

        # Set orientation
        [rX, rY, rZ] = object.getOrientation()
        self.orientationInputP.setText(str(rX))
        self.orientationInputY.setText(str(rY))
        self.orientationInputR.setText(str(rZ))

        # Set color
        (r, g, b, a) = object.getColor()
        self.redInput.setValue(int(r))
        self.greenInput.setValue(int(g))
        self.blueInput.setValue(int(b))

        # Set other
        self.setOther(object)

    def setBlank(self):
        self.nameInput.setText('')

    def onNameChange(self, s: str):
        self.selectedObject.updateName(s)

    def onTranslationChange(self, s):
        self.selectedObject.setTranslation(float(self.translationInputX.text()), 
                                        float(self.translationInputY.text()),
                                        float(self.translationInputZ.text()))
    
    def onOrientationChange(self, s):
        self.selectedObject.setOrientation(float(self.orientationInputR.text()), 
                                        float(self.orientationInputP.text()),
                                        float(self.orientationInputY.text()))

    def onColorChange(self, c):
        self.selectedObject.setColor(self.redInput.value(), self.greenInput.value(), self.blueInput.value())

    def focusNameInput(self):
        self.nameInput.setFocus()

    def setOther(self, object):
        pass