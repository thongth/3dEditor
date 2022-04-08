class ThreeDObject():
    def __init__(self, name, rootEntity):
        self.name = name
        self.rootEntity = rootEntity

    def updateName(self, name):
        self.name = name