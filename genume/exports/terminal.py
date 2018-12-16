from genume.registry.registry import Registry
from genume.registry.category import CategoryEntry
from genume.exports.exporter import Exporter


class TextExporter(Exporter):

    def __init__(self):
        super().__init__("text")

    def handle(self, root, level):
        text = ""
        for k, v in root.items():
            if isinstance(v, CategoryEntry):
                text += "{0}{1}: {2}\n".format("\t" * level, k, v.desc)
                text += self.handle(v, level + 1)
            else:
                text += "{0}{1}: {2}\n".format("\t" * level, k, v)

        return text
