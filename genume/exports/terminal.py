from genume.registry.registry import Registry
from genume.registry.category import CategoryEntry


def print_enumeration(e, level=0):
    """Dumps the tree of entries to stdout."""
    for k, v in e.items():
        if isinstance(v, CategoryEntry):
            print("{0}{1}:".format("\t" * level, k))
            print_enumeration(v, level + 1)
        else:
            print("{0}{1}: {2}".format("\t" * level, k, v))


def main():
    registry = Registry()
    registry.update()
    print_enumeration(registry.root)
