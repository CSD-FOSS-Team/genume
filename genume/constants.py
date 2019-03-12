import os.path
import multiprocessing

# A string with the name of this program
NAME = "genume"

# A string containing a small description of this program.
DESC = "Graphical ENUMEration"

# A string representing our current version.
VERSION = "0.1.2"

# Package file. Used for packaging the scripts when installing
GENUME_PACK = os.path.join(os.path.dirname(os.path.realpath(__file__)), "package.tar")

# Is genume running in release mode?
GENUME_RELEASE = os.path.isfile(GENUME_PACK)

# Path of where the scripts and bash helper folders are. Differs between development and release.
GENUME_ROOT = os.path.expanduser("~/.cache/genume/") if GENUME_RELEASE else os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir)

# Log filepath or None to disable logging to file.
LOGGER_FILE = os.path.join(GENUME_ROOT, "genume.log")

# Log format string.
LOGGER_FMT = "%(asctime)s [%(levelname)s|%(threadName)s] %(message)s"

# Log date format string.
LOGGER_DATE_FMT = "%H:%M:%S"

# Path of the scripts folder.
SCRIPTS_ROOT = os.path.join(GENUME_ROOT, "scripts")

# A list of ignored files when searching for scripts.
SCRIPTS_IGNORE = [r"__pycache__", r"^\..+", r".*\.md$", r".*\.log$"]

# Extra executables for bash folder.
SCRIPTS_BASH_EXTRA = os.path.join(GENUME_ROOT, "bash_helpers")

# Limit the maximum number of child processes to have running at any given time.
# This limit is imposed by each instance of Registry separately.
SCRIPTS_MAX_MULTI_DISPATCH = max(min(multiprocessing.cpu_count(), 32), 4)

# Assets folder. Used by the view.
ASSETS_ROOT = os.path.join(os.path.dirname(__file__), "view/assets")

# The path to the logo.
# The logo image must be 200X100 px
ASSETS_LOGO = os.path.join(ASSETS_ROOT, "logo.png")

# The path to the refresh icon.
ASSETS_REFRESH = os.path.join(ASSETS_ROOT, "icon_refresh.png")
