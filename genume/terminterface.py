# For now test code.
from .registry.registry import Registry

print(__name__)
reg = Registry()
reg.update()
print(reg.root)