import os.path
import multiprocessing

# A string with the name of this program
NAME = "genume"

# A string containing a small description of this program.
DESC = "Graphical ENUMEration"

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

# Extra executables for bash folder.
SCRIPTS_BASH_EXTRA = os.path.dirname(os.path.realpath(__file__)) + "/../" + "bash_helpers/"

# Limit the maximum number of child processes to have running at any given time.
# This limit is imposed by each instance of Registry separately.
SCRIPTS_MAX_MULTI_DISPATCH = multiprocessing.cpu_count()
