from enum import Enum

# Base classes and other objects.

InfoLevel = Enum("InfoLevel", "basic advanced")

class BaseEntry:
    "Common base class for all registry entries."
    def __init__(self, parent=None, level=InfoLevel.basic):
        if parent is None or isinstance(parent, BaseEntry):
            self.parent = None
            self.level = level
        else:
            raise RuntimeError("Error: tried to create an entry with an invalid parent.")
