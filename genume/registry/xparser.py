from shlex import split as cmdsplit
import subprocess as sbpr
import os

from genume.constants import VERSION
from genume.registry.base import InfoLevel
from genume.registry.value import ValueEntry, ListEntry
from genume.registry.category import CategoryEntry


def parse(cmdl, c):
    root_c = c

    while len(cmdl) != 0:

        command = cmdl.pop(0)
        level = cmdl.pop(0)
        key = cmdl.pop(0)

        if command == "VALUE" or command == "VALUES":
            value = cmdl.pop(0).strip()

            path = None
            if len(cmdl) >= 2:
                if cmdl[0] == "GROUP" and cmdl[1] != "BAS" and cmdl[1] != "ADV":
                    cmdl.pop(0)
                    path = parse_path(cmdl.pop(0), False)
                elif cmdl[0] == "PATH" and cmdl[1] != "BAS" and cmdl[1] != "ADV":
                    cmdl.pop(0)
                    path = parse_path(cmdl.pop(0), True)

            parent = get_category_from_path(root_c, path) if path is not None else c

            if command == "VALUE":
                # basic value case.
                value = ValueEntry(parent, value)
                if level == "ADV":
                    value.level = InfoLevel.advanced
                parent[key] = value

            elif command == "VALUES":
                # entry of list
                if key in parent:
                    parent[key].add(value)
                else:
                    level = ListEntry(parent, value)
                    if level == "ADV":
                        level.level = InfoLevel.advanced
                    parent[key] = level

        elif command == "GROUP" or command == "PATH":

            if key == ".":
                c = root_c
            else:
                path = parse_path(key, command == "PATH")
                c = get_category_from_path(root_c, path, level)

        else:
            print("Warn: invalid command {0}".format(command))


def parse_path(path, split):
    # path from string to array
    return path.split(".") if split else [path]


def get_category_from_path(category, path, level=InfoLevel.basic):
    c = category
    for i in path:
        # create new category if missing
        if i not in c:
            new_category = CategoryEntry(c)
            c[i] = new_category

        # move along
        c = c[i]

    return c


def run(f):
    if os.access(str(f), os.X_OK):
        o = sbpr.check_output(str(f))
        s = o.decode("utf-8").strip()
        return s
    else:
        print("Warn: {0} is not executable.".format(str(f)))


def run_and_parse(cat, file):
    s = run(file)
    if s:
        parse(cmdsplit(s), cat)


# Initialize environment variables.
# TODO move elsewhere
os.putenv("GENUME_VERSION", VERSION)
