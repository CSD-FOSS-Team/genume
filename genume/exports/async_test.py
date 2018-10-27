import logging as log
import time

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


class ASyncExporter(Exporter):

    def __init__(self):
        super().__init__("async")

    def export(self, reg):
        text = ""
        log.info("Starting registry refresh...")
        reg.request_refresh()
        time.sleep(8)
        return text
