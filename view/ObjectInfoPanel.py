from PySide2.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QLabel, QLineEdit, QSlider
from PySide2.QtCore import Qt

class ObjectInfoPanel(QWidget):
    def __init__(self, parent=None):
        super(ObjectInfoPanel, self).__init__(parent)
        self.selectedObject = None
        layout = QVBoxLayout()
        layout.setContentsMargins(0,0,0,0)

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

        # Radius
        self.radiusLayout = QHBoxLayout()
        self.radiusLabel = QLabel("Radius")
        self.radiusInput = QSlider(Qt.Horizontal)
        self.radiusInput.setMinimum(1)
        self.radiusInput.setMaximum(10)
        self.radiusInput.sliderMoved.connect(self.onRadiusChange)
        self.radiusLayout.addWidget(self.radiusLabel)
        self.radiusLayout.addWidget(self.radiusInput)

        layout.addLayout(self.nameLayout)
        layout.addLayout(self.translationLayout)
        layout.addLayout(self.orientationLayout)
        layout.addLayout(self.redLayout)
        layout.addLayout(self.greenLayout)
        layout.addLayout(self.blueLayout)
        layout.addLayout(self.radiusLayout)

        self.setLayout(layout)

    def setSelectedObject(self, selectedObject):
        self.selectedObject = selectedObject
        self.setPlaceHolder(self.selectedObject)

    def setPlaceHolder(self, object):
        if object == None:
            self.setBlank()
            return
        self.nameInput.setText(object.name)
        self.translationInputX.setText(str(object.getTranslation().x()))
        self.translationInputY.setText(str(object.getTranslation().y()))
        self.translationInputZ.setText(str(object.getTranslation().z()))
        [rX, rY, rZ] = object.getOrientation()
        self.orientationInputP.setText(str(rX))
        self.orientationInputY.setText(str(rY))
        self.orientationInputR.setText(str(rZ))
        self.radiusInput.setValue(int(object.getRadius()))
        (r, g, b, a) = object.getColor()
        self.redInput.setValue(int(r))
        self.greenInput.setValue(int(g))
        self.blueInput.setValue(int(b))

    def setBlank(self):
        self.nameInput.setText('')

    def onNameChange(self, s):
        self.selectedObject.updateName(s)

    def onTranslationChange(self, s):
        self.selectedObject.setTranslation(float(self.translationInputX.text()), 
                                        float(self.translationInputY.text()),
                                        float(self.translationInputZ.text()))
    
    def onOrientationChange(self, s):
        self.selectedObject.setOrientation(float(self.orientationInputR.text()), 
                                        float(self.orientationInputP.text()),
                                        float(self.orientationInputY.text()))

    def onRadiusChange(self, r):
        self.selectedObject.setRadius(r)

    def onColorChange(self, c):
        self.selectedObject.setColor(self.redInput.value(), self.greenInput.value(), self.blueInput.value())