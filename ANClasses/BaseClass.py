class NewerCPPFunction(object):
    def __init__(self):
        super().__init__()
        self.validTransformArgs = []
        self.header = ""
        self.footer = ""
        self.title = ""

        self.blocks = []
        self.blockPackedData = []



class NewerCPPClass(object):
    def __init__(self):
        super().__init__()
        self.classDisplayName = "Empty class"
        self.classInternalName = "EmptyClass"
        self.header = ""
        self.footer = ""
        self.functions = []