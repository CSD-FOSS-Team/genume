import os
import argparse

import genume.view.main as gui
from genume.constants import NAME, DESC, VERSION
from genume.registry.registry import Registry
from genume.exports.terminal import TextExporter
from genume.exports.json import JsonExporter, JsonPrettyExporter
from genume.exports.html import HtmlExporter


def main():
    exporters = gen_exporters()

    parser = argparse.ArgumentParser(prog=NAME, description=DESC)

    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + VERSION)

    export_group = parser.add_mutually_exclusive_group()
    for k in sorted(exporters.keys()):
        export_group.add_argument('--' + k, dest='export', action='store_const',
                                  const=k, help='exports in ' + k + ' format')

    args = parser.parse_args()

    if args.export is None:
        # Check if a graphical environment is available(X11 or Wayland).
        if "DISPLAY" in os.environ or "WAYLAND_DISPLAY" in os.environ:
            gui.main()
        else:
            print("Could not detect a graphical environment!")
    else:
        registry = Registry()
        registry.refresh()
        print(exporters[args.export].export(registry))


def gen_exporters():
    # a list of all the available export methods
    list = [TextExporter(), JsonExporter(), HtmlExporter(), JsonPrettyExporter()]
    # generate a name to export map
    map = {i.name: i for i in list}
    return map
