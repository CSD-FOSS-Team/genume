from genume.registry.base import BaseEntry

class ValueEntry(BaseEntry):
    "A type of entry which contains a single string."
    def __init__(self, parent=None, value=""):
        super().__init__(parent)
        self.value = value
    def __repr__(self):
        return self.value
