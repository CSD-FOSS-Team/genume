import logging as log

from genume.registry.base import BaseEntry, InfoLevel
from genume.registry.category import CategoryEntry
from genume.registry.value import ValueEntry
from genume.utils import find_executable


def __get_category_from_path(root, path):
    # Start from the root.
    current = root
    for p in path:
        current = current[p]
    return current


def __get_category_from_state(root, state):
    path = state.get("path")
    if path is not None:
        return __get_category_from_path(root, path)
    else:
        return root


def __parse_path(path, state):
    # Break down path into components.
    parsed = path.split(".")
    # Handles empty and relative paths.
    if(len(parsed[0]) == 0):
        parsed.pop(0)
        parsed = state.get("path", []) + parsed
    # Remove empty items(usually caused by double lines).
    parsed = [x for x in parsed if len(x) != 0]
    return parsed


def __create_categories_from_path(root, path, info_level):
    curcat = root
    for e in path:
        if curcat.get(e) is None:
            curcat[e] = CategoryEntry(curcat, info_level)
        curcat = curcat[e]


def __info_level_from_string(string):
    return InfoLevel.advanced if string == "ADV" else InfoLevel.basic


def parse_conf(arguments, main_category, observer, state):
    for e in arguments:
        if e == "root":
            return "root is not supported yet!"
        elif find_executable(e) is None:
            return e + " may not be installed!"
    return "OK"


def parse_set(args, mc, obs, state):
    type_arg = args.pop(0)
    if type_arg == "DESCRIPTION":
        if len(args) == 1:
            value = args.pop(0)
            target = __get_category_from_state(mc, state)
            target.desc = value
        else:
            log.warning("SET %s: requires only one argument, got %d" % (type_arg, len(args)))
    else:
        log.warning("SET %s: unknown key" % (type_arg))


def parse_value(args, mc, obs, state):
    info_level = InfoLevel.basic
    path = state.get("path", [])
    scan_values = False
    scan_path = False
    entry = None
    for e in args:
        if not scan_values and not scan_path:
            if e == "BAS" or e == "ADV":
                info_level = __info_level_from_string(e)
            elif e == "SUBCAT":
                scan_path = True
            else:
                key = e
                # Find entry by key and then switch to adding values to it.
                cat = __get_category_from_path(mc, path)
                entry = cat.get(key)
                if entry is None:
                    entry = ValueEntry(cat, info_level)
                    cat[key] = entry
                scan_values = True
        elif scan_path:
            path = __parse_path(e, state)
            # Make sure the path exists.
            __create_categories_from_path(mc, path, info_level)
            scan_path = False
        elif scan_values:
            entry.add(e.strip())


def parse_subcat(args, mc, obs, state):
    info_level = InfoLevel.basic
    path = None
    # Parse arguments.
    if len(args) == 1:
        path = args[0]
    elif len(args) == 2:
        info_level = __info_level_from_string(args[0])
        path = args[1]
    else:
        log.warning("SUBCAT: 1 or 2 positional arguments required! Got %d arguments." % (len(args)))
        return
    # Init state if not already initialized.
    if state.get("path") is None:
        state["path"] = []
    parsed = __parse_path(path, state)
    # Save state
    state["path"] = parsed
    # Create any new CategoryEntries.
    __create_categories_from_path(mc, parsed, info_level)


COMMAND_REGISTRY = {
    "CONF": parse_conf,
    "SET": parse_set,
    "VALUE": parse_value,
    "SUBCAT": parse_subcat, "PATH": parse_subcat
}
