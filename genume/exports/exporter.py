

class Exporter:

    def __init__(self, name):
        self.name = name

    def export(self, reg):
        return self.handle(reg.root, 0)

    def handle(self, root, level):
        pass
