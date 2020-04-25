import logging as log
from sys import stderr

from genume.constants import LOGGER_FILE, LOGGER_FMT, LOGGER_DATE_FMT


class ColoredFormatter(log.Formatter):
    """Log messages with ascii colors."""
    RED = "\x1B[31m"
    GREEN = "\x1B[32m"
    YELLOW = "\x1B[33m"
    BLUE = "\x1B[34m"
    MAGENTA = "\x1B[35m"
    CYAN = "\x1B[36m"
    WHITE = "\x1B[37m"
    RESET = "\x1B[0m"
    LEVEL2COLOR = {log.NOTSET: WHITE, log.DEBUG: BLUE, log.INFO: GREEN,
                   log.WARNING: CYAN, log.ERROR: YELLOW, log.CRITICAL: RED}

    def format(self, record):
        msg = super().format(record)
        level = record.levelno
        color = ColoredFormatter.LEVEL2COLOR.get(level, ColoredFormatter.LEVEL2COLOR[log.NOTSET])
        return color + msg + ColoredFormatter.RESET


def init(level=log.DEBUG):
    """This function sets up logging. It needs to be called very early in the program."""
    rootLogger = log.getLogger()
    rootLogger.setLevel(level)
    # File output.
    if LOGGER_FILE is not None:
        fileHndl = log.FileHandler(LOGGER_FILE, mode="w")
        fileFmt = log.Formatter(fmt=LOGGER_FMT, datefmt=LOGGER_DATE_FMT)
        fileHndl.setFormatter(fileFmt)
        rootLogger.addHandler(fileHndl)
    # Terminal output.
    termHndl = log.StreamHandler(stream=stderr)
    termFmt = ColoredFormatter(fmt=LOGGER_FMT, datefmt=LOGGER_DATE_FMT)
    termHndl.setFormatter(termFmt)
    rootLogger.addHandler(termHndl)
