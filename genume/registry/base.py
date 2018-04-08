class BaseEntry:
    "Common base class for all registry entries."
    def __init__(self, parent=None):
        if parent is None or isinstance(parent, BaseEntry):
            self.parent = None
        else:
            print("Error: tried to create an entry with an invalid parent.")
    # TODO: Importance level? User can select between basic and advanced info.
