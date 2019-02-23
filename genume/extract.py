import tarfile
import logging as log

from genume.constants import GENUME_RELEASE, GENUME_ROOT, GENUME_PACK


def extract():
    if GENUME_RELEASE:
        tar = tarfile.open(GENUME_PACK)
        tar.extractall(path=GENUME_ROOT)
        tar.close()
