import os.path
import multiprocessing

# A string representing our current version.
VERSION = "0.1.2"

# Log filepath or None to disable logging to file.
LOGGER_FILE = "genume.log"

# Log format string.
LOGGER_FMT = "%(asctime)s [%(levelname)s|%(threadName)s] %(message)s"

# Log date format string.
LOGGER_DATE_FMT = "%H:%M:%S"

# Path of the scripts folder.
SCRIPTS_ROOT = os.path.dirname(os.path.realpath(__file__)) + "/../" + "scripts/"

# A list of ignored files when searching for scripts.
SCRIPTS_IGNORE = [r"__pycache__", r"^\..+", r".*\.md$"]

# Limit the maximum number of child processes to have open at the same time.
MAX_MULTIEXE = multiprocessing.cpu_count()

# A list of preinstalled executables in the sandbox.
PREINSTALLED_DEPS = ("cat", "grep")
