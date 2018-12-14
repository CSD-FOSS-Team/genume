import re

# Random methods used by the rest of the program.


def find_key_of_value(d, v):
    "Founds the key of a value stored in a dictionary."
    return list(d.keys())[list(d.values()).index(v)]


def match_list(s, l):
    "Match any in a list 'l' (with regex 's')."
    for i in l:
        if re.match(i, s):
            return True
    return False


def merge_dicts(a, b):
    "Merge two dictionaries."
    c = a.copy()
    c.update(b)
    return c
