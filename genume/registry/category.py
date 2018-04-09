from collections import OrderedDict
from .base import BaseEntry

class Category(BaseEntry, OrderedDict):
    "A registry entry which acts as a container for other entries."
