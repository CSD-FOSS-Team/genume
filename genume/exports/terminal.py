from genume.registry.registry import Registry
from genume.registry.category import CategoryEntry
from genume.exports.exporter import Exporter


def print_enumeration(e, level=0):
    """Dumps the tree of entries to stdout."""
    for k, v in e.items():
        if isinstance(v, CategoryEntry):
            print("{0}{1}:".format("\t" * level, k))
            print_enumeration(v, level + 1)
        else:
            print("{0}{1}: {2}".format("\t" * level, k, v))


class TextExporter(Exporter):

    def __init__(self):
        super().__init__("text")

    def handle(self, root, level):
        text = ""
        for k, v in root.items():
            if isinstance(v, CategoryEntry):
                text += "{0}{1}:\n".format("\t" * level, k)
                text += self.handle(v, level + 1)
            else:
                text += "{0}{1}: {2}\n".format("\t" * level, k, v)

        return text
