import os
import sys
import argparse
import logging as log
from pathlib import Path

from genume.view.main import MainWindow
from genume.constants import NAME, DESC, VERSION, SCRIPTS_ROOT
from genume.registry.registry import Registry
from genume.exports.terminal import TextExporter
from genume.exports.json import JsonExporter, JsonPrettyExporter
from genume.exports.html import HtmlExporter


def main():
    exporters = gen_exporters()

    parser = argparse.ArgumentParser(prog=NAME, description=DESC)

    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + VERSION)
    parser.add_argument('-q', '--quiet', dest='quiet', action='store_true', help="Only print errors.")
    parser.add_argument('-V', '--verbose', dest='verbose', action='store_true', help="Print everything.")
    parser.add_argument('--no-titlebar', dest='titlebar', action='store_false', help="Disables custom titlebar.")
    parser.add_argument('--output', dest='output', type=str, action='store', help="Where to save the export.")
    parser.add_argument('-r', '--scripts-root', dest='scripts_root', type=str, action='store', default=SCRIPTS_ROOT,
                        help="Load scripts form a specified directory.")

    export_group = parser.add_mutually_exclusive_group()
    for k in sorted(exporters.keys()):
        export_group.add_argument('--' + k, dest='export', action='store_const',
                                  const=k, help='exports in ' + k + ' format')

    args = parser.parse_args()

    log.getLogger().setLevel(log.INFO)
    if args.verbose:
        log.getLogger().setLevel(log.DEBUG)
    if args.quiet:
        log.getLogger().setLevel(log.ERROR)

    scripts_path = Path(args.scripts_root).expanduser()
    if not scripts_path.exists():
        print("Path '{0}' does not exist!".format(scripts_path))
        sys.exit(2)

    if args.export is None:
        # Check if a graphical environment is available(X11 or Wayland).
        if "DISPLAY" in os.environ or "WAYLAND_DISPLAY" in os.environ:
            registry = Registry(scripts_path)
            gui = MainWindow(registry, titlebar=args.titlebar)
        else:
            print("Could not detect a graphical environment!")
    else:
        registry = Registry(scripts_path)
        registry.refresh()
        export_string = exporters[args.export].export(registry)
        if args.output is None:
            print(export_string)
        else:
            f = open(args.output, "w")
            f.write(export_string)
            f.close()


def gen_exporters():
    # a list of all the available export methods
    list = [TextExporter(), JsonExporter(), HtmlExporter(), JsonPrettyExporter()]
    # generate a name to export map
    map = {i.name: i for i in list}
    return map
