from collections import OrderedDict

from genume.registry.base import BaseEntry

class CategoryEntry(BaseEntry, OrderedDict):
    "A registry entry which acts as a container for other entries."