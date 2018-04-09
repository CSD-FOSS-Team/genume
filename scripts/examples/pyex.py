from genume.registry.base import PythonScript
from genume.registry.value import ValueEntry

class PYEX(PythonScript):
    "Example python script."
    def run(self):
        print("Script running!!!")
        self.register("pytest", ValueEntry(self.category, "Python script test."))