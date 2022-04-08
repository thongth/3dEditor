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
        self.translationLayout.addWidget(self.translationLabel)
        self.translationLayout.addWidget(self.translationInputX)
        self.translationLayout.addWidget(self.translationInputY)
        self.translationLayout.addWidget(self.translationInputZ)

        # Translation
        self.orientationLayout = QHBoxLayout()
        self.orientationLabel = QLabel("Orientation")
        self.orientationInputR = QLineEdit()
        self.orientationInputP = QLineEdit()
        self.orientationInputY = QLineEdit()
        self.orientationLayout.addWidget(self.orientationLabel)
        self.orientationLayout.addWidget(self.orientationInputR)
        self.orientationLayout.addWidget(self.orientationInputP)
        self.orientationLayout.addWidget(self.orientationInputY)

        # Radius
        self.radiusLayout = QHBoxLayout()
        self.radiusLabel = QLabel("Radius")
        self.radiusInput = QSlider(Qt.Horizontal)
        self.radiusInput.setMinimum(1)
        self.radiusInput.setMaximum(10)
        self.radiusLayout.addWidget(self.radiusLabel)
        self.radiusLayout.addWidget(self.radiusInput)

        layout.addLayout(self.nameLayout)
        layout.addLayout(self.translationLayout)
        layout.addLayout(self.orientationLayout)
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

    def setBlank(self):
        self.nameInput.setText('')

    def onNameChange(self, s):
        self.selectedObject.updateName(s)