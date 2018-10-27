import argparse

import genume.view.main as gui
from genume.registry.registry import Registry
from genume.exports.terminal import TextExporter
from genume.exports.async_test import ASyncExporter
from genume.exports.json import JsonExporter, JsonPrettyExporter
from genume.exports.html import HtmlExporter

# Also check if we are running inside a virtual console.
# Then just dump the registry to stdout.


def main():
    exporters = gen_exporters()

    parser = argparse.ArgumentParser(prog='genume', description='genume - graphical enumeration')

    export_group = parser.add_mutually_exclusive_group()
    for k in sorted(exporters.keys()):
        export_group.add_argument('--' + k, dest='export', action='store_const',
                                  const=k, help='exports in ' + k + ' format')

    args = parser.parse_args()

    if args.export is None:
        gui.main()
    else:
        registry = Registry()
        registry.refresh()
        print(exporters[args.export].export(registry))


def gen_exporters():
    # a list of all the available export methods
    list = [TextExporter(), ASyncExporter(), JsonExporter(), HtmlExporter(), JsonPrettyExporter()]
    # generate a name to export map
    map = {i.name: i for i in list}
    return map
