import argparse

import genume.view.main as gui
from genume.registry.registry import Registry
from genume.exports.terminal import TextExporter
from genume.exports.json import JsonExporter, JsonPrettyExporter
from genume.exports.html import HtmlExporter

# TODO: Argument checking will go here.
# Also check if we are running inside a virtual console.
# Then just dump the registry to stdout.


def main():
    exporters = gen_exporters()

    parser = argparse.ArgumentParser(description='genume')

    for k in exporters.keys():
        parser.add_argument('--' + k, dest='export', action='store_const',
                            const=k, help='exports in ' + k + ' format')

    args = parser.parse_args()

    if args.export is None:
        gui.main()
    else:
        registry = Registry()
        registry.update()
        print(exporters[args.export].export(registry))


def gen_exporters():
    # a list of all the available export methods
    list = [TextExporter(), JsonExporter(), HtmlExporter(), JsonPrettyExporter()]
    # generate a name to export map
    map = {i.name: i for i in list}
    return map
