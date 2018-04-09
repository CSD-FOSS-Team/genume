from enum import Enum

EnumLevel = Enum("EnumLevel", "basic advanced")

class BaseEntry:
    "Common base class for all registry entries."
    def __init__(self, parent=None, level=EnumLevel.basic):
        if parent is None or isinstance(parent, BaseEntry):
            self.parent = None
            self.level = level
        else:
            print("Error: tried to create an entry with an invalid parent.")
