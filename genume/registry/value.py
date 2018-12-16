from genume.registry.base import BaseEntry, InfoLevel


class ValueEntry(BaseEntry):
    """A entry which contains a list of strings"""

    def __init__(self, parent=None, level=InfoLevel.basic, value=None):
        super().__init__(parent, level)
        if value is None:
            self.values = []
        else:
            self.values = [value]

    def add(self, value):
        self.values.append(value)

    def __repr__(self):
        return '\n'.join(self.values)

    def __str__(self):
        return '[' + ', '.join(self.values) + ']'
