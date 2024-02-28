class Vertex:
    def __init__(self, _name = None, _info = None):
        self.name = _name
        if _info is None:
            self.info = {}  # Or any other suitable default mutable object
        else:
            self.info = _info.copy()

    def setInfo(self, _info):
        self.info = _info.copy()



