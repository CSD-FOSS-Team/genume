print(__name__)
import sys
print(sys.path)
def run(cat, entries):
    # from registry.value import ValueEntry
    # Test script.
    print("Running...")
    nkv = entries["ValueEntry"](cat, "Testing from python.")
    cat["python"] = nkv