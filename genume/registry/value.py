from genume.registry.base import BaseEntry


class ValueEntry(BaseEntry):
    """A type of entry which contains a single string."""

    def __init__(self, parent=None, value=""):
        super().__init__(parent)
        self.value = value

    def __repr__(self):
        return self.value


class ListEntry(BaseEntry):
    """A entry which contains a list of strings"""

    def __init__(self, parent=None, value=None):
        super().__init__(parent)
        if value is None:
            self.values = []
        else:
            self.values = [value]

    def add(self, value):
        self.values.append(value)

    def __repr__(self):
        return '[' + ', '.join(self.values) + ']'
