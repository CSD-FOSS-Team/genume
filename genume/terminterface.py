from genume.registry.registry import Registry
from genume.registry.category import CategoryEntry

# A simple script which runs the enumeration
# and then dumps the resulting registry in stdout
def print_enumeration(e, l=0):
    for k, v in e.items():
        if isinstance(v, CategoryEntry):
            print("{0}{1}:".format("\t"*l, k))
            print_enumeration(v, l + 1)
        else:
            print("{0}{1}: {2}".format("\t"*l, k, v))

def run():
    registry = Registry()
    print("###########################\nUpdating enumeration...")
    registry.update()
    print("Updated enumeration!!!\n###########################")
    print_enumeration(registry.root)