from PySide2.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QLabel, QLineEdit, QSlider
from PySide2.QtCore import Qt

class ObjectInfoPanel(QWidget):
    def __init__(self, parent=None):
        super(ObjectInfoPanel, self).__init__(parent)
        layout = QVBoxLayout()
        layout.setContentsMargins(0,0,0,0)

        # Name
        nameLayout = QHBoxLayout()
        nameLabel = QLabel("Name")
        nameInput = QLineEdit()
        nameLayout.addWidget(nameLabel)
        nameLayout.addWidget(nameInput)

        # Translation
        translationLayout = QHBoxLayout()
        translationLabel = QLabel("Translation")
        translationInputX = QLineEdit()
        translationInputY = QLineEdit()
        translationInputZ = QLineEdit()
        translationLayout.addWidget(translationLabel)
        translationLayout.addWidget(translationInputX)
        translationLayout.addWidget(translationInputY)
        translationLayout.addWidget(translationInputZ)

        # Translation
        orientationLayout = QHBoxLayout()
        orientationLabel = QLabel("Orientation")
        orientationInputR = QLineEdit()
        orientationInputP = QLineEdit()
        orientationInputY = QLineEdit()
        orientationLayout.addWidget(orientationLabel)
        orientationLayout.addWidget(orientationInputR)
        orientationLayout.addWidget(orientationInputP)
        orientationLayout.addWidget(orientationInputY)

        # Radius
        radiusLayout = QHBoxLayout()
        radiusLabel = QLabel("Radius")
        radiusInput = QSlider(Qt.Horizontal)
        radiusInput.setMinimum(1)
        radiusInput.setMaximum(10)
        radiusLayout.addWidget(radiusLabel)
        radiusLayout.addWidget(radiusInput)

        layout.addLayout(nameLayout)
        layout.addLayout(translationLayout)
        layout.addLayout(orientationLayout)
        layout.addLayout(radiusLayout)

        self.setLayout(layout)