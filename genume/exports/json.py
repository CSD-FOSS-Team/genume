
import json
from genume.exports.exporter import Exporter
from genume.registry.category import CategoryEntry
from genume.registry.value import ValueEntry


class JsonExporterBase(Exporter):

    def handle(self, root, level):
        return self.json_dump(self.sub_handle(root))

    def json_dump(self, object):
        pass

    def sub_handle(self, root):
        o = {}
        for k, v in root.items():
            if isinstance(v, CategoryEntry):
                o[k] = self.sub_handle(v)
            else:
                o[k] = str(v)

        return o


class JsonExporter(JsonExporterBase):

    def __init__(self):
        super().__init__("json-min")

    def json_dump(self, object):
        return json.dumps(object)


class JsonPrettyExporter(JsonExporterBase):

    def __init__(self):
        super().__init__("json")

    def json_dump(self, object):
        return json.dumps(object, indent=2, sort_keys=True)
