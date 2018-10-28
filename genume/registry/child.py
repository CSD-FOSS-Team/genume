from shlex import split as cmdsplit
import subprocess as sbpr
import logging as log
import os

from genume.constants import VERSION
from genume.registry.category import CategoryEntry


def find_key_of_value(d, v):
    "Founds the key of a value stored in a dictionary."
    return list(d.keys())[list(d.values()).index(v)]


class ChildHandler:
    """Handles child lifecycle and command parsing."""

    def __init__(self, path, root_cat):
        self.path = path
        self.root = root_cat
        self.shadow = CategoryEntry()
        self.done = False

    def generate_env(self):
        "Generates the environment variables that are passed to the child"
        name = "root"
        if root.parent is not None:
            name = find_key_of_value(root.parent, root)
        extra_env = {"GENUME_VERSION": VERSION, "MASTER_CATEGORY": name}
        return {**extra_env, **os.environ}

    def start(self):
        "Prepares and launches the child."
        child = sbpr.Popen(args=str(self.path), shell=False, bufsize=1, universal_newlines=True,
                           stdin=sbpr.PIPE, stdout=sbpr.PIPE, close_fds=False, env=self.generate_env)
        log.info("Started new child with pid %i" % (child.pid))
        self.executable = child

    def do_step(self):
        "Performs one command proccessing step. Returns true if the command finished execution else false."
        pass

    def has_been_killed(self):
        "Returns true when this child has finished execution."
        return self.done
