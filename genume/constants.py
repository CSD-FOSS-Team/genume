import os.path

# A string representing our current version.
VERSION = "0.1.1"

# Path of the scripts folder.
SCRIPTS_ROOT = os.path.dirname(os.path.realpath(__file__)) + "/../" + "scripts/"

# A list of ignored files when searching for scripts.
SCRIPTS_IGNORE = [r"__pycache__", r"^\..+", r".*\.md$"]
