
from genume.exports.exporter import Exporter
from genume.registry.category import CategoryEntry


class HtmlExporter(Exporter):

    def __init__(self):
        super().__init__("html")

    def handle(self, root, level):
        html = "<ul>\n"
        for k, v in root.items():
            if isinstance(v, CategoryEntry):
                html += "<li><span class=\"name\">{0}</span>\n".format(k)
                html += self.handle(v, level + 1)
                html += "</li>"
            else:
                html += "<li><span class=\"name\">{0}</span> <span class=\"value\">{1}</span></li>\n".format(k, v)
        html += "</ul>\n"

        return html
