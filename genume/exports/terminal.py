from genume.registry.registry import Registry
from genume.registry.category import CategoryEntry


def print_enumeration(e, l=0):
    """Dumps the tree of entries to stdout."""
    for k, v in e.items():
        if isinstance(v, CategoryEntry):
            print("{0}{1}:".format("\t" * l, k))
            print_enumeration(v, l + 1)
        else:
            print("{0}{1}: {2}".format("\t" * l, k, v))


def main():
    registry = Registry()
    registry.update()
    print_enumeration(registry.root)
