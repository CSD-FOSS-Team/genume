from collections.abc import MutableMapping
from collections import OrderedDict

from genume.registry.base import BaseEntry, InfoLevel


class CategoryEntry(BaseEntry, MutableMapping):
    """A registry entry which acts as a container for other entries."""
    def __init__(self, parent=None, level=InfoLevel.basic, path=None, description=""):
        self.desc = description
        self.storage = OrderedDict()
        self.path = path
        super().__init__(parent, level)

    def __getitem__(self, key):
        return self.storage[self.__keytransform__(key)]

    def __setitem__(self, key, value):
        self.storage[self.__keytransform__(key)] = value

    def __delitem__(self, key):
        del self.storage[self.__keytransform__(key)]

    def __iter__(self):
        return iter(self.storage)

    def __len__(self):
        return len(self.storage)

    def __keytransform__(self, key):
        return key

    def merge(self, entry):
        if entry.desc is not None and entry != "":
            self.desc = entry.desc
        self.update(entry)
