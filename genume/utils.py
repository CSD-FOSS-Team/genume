import re
import os

from genume.constants import SCRIPTS_AVERAGE_MEM_USAGE

# Random methods used by the rest of the program.


def find_key_of_value(d, v):
    "Founds the key of a value stored in a dictionary."
    return list(d.keys())[list(d.values()).index(v)]


def match_list(s, ll):
    "Match any in a list 'll' (with regex 's')."
    for i in ll:
        if re.match(i, s):
            return True
    return False


def merge_dicts(a, b):
    "Merge two dictionaries."
    c = a.copy()
    c.update(b)
    return c


def make_signal_emitter(gobj, signal):
    "Creates a one time signal emitter for use with GLib.idle_add()."
    def _emitter():
        gobj.emit(signal)
        return False
    return _emitter


def find_executable(name):
    "Finds the path of an executable. Returns None if the executable could not be found."
    paths = os.environ["PATH"].split(':')
    for path in paths:
        if os.path.isdir(path) and name in os.listdir(path):
            return path + "/" + name
    return None


def get_available_memory():
    """Returns the available/usable memory in kB."""
    with open("/proc/meminfo", 'r') as mem:
        for s in mem:
            comps = s.split()
            if str(comps[0]) == "MemAvailable:":
                return int(comps[1])
    return 0


def get_scripts_multidispatch_limit():
    avail = get_available_memory() * 0.8
    limit = avail / SCRIPTS_AVERAGE_MEM_USAGE
    return max(int(limit), 16)
