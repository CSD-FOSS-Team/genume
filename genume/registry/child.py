from shlex import split as cmdsplit
import subprocess as sbpr
import logging as log
import time
import os

from genume.constants import VERSION
from genume.registry.category import CategoryEntry


def find_key_of_value(d, v):
    "Founds the key of a value stored in a dictionary."
    return list(d.keys())[list(d.values()).index(v)]


def parse_conf(stack, root, state):
    pass


def parse_set(stack, root, state):
    pass


def parse_value(stack, root, state):
    pass


def parse_subcat(stack, root, state):
    pass


COMMAND_REGISTRY = {"CONF": parse_conf, "SET": parse_set,
                    "VALUE": parse_value, "SUBCAT": parse_subcat}


class ChildHandler:
    """Handles child lifecycle and command parsing."""

    def __init__(self, path, root_cat):
        self.path = path
        self.root = root_cat
        self.shadow = CategoryEntry()
        self.state = {}
        self.done = False

    def generate_env(self):
        "Generates the environment variables that are passed to the child"
        name = "root"
        if self.root.parent is not None:
            name = find_key_of_value(root.parent, root)
        extra_env = {"GENUME_VERSION": VERSION, "MASTER_CATEGORY": name}
        return {**extra_env, **os.environ}

    def start(self):
        "Prepares and launches the child."
        child = sbpr.Popen(args=str(self.path), shell=False, bufsize=0, universal_newlines=True,
                           stdin=sbpr.PIPE, stdout=sbpr.PIPE, close_fds=False, env=self.generate_env())
        log.info("Started child \"%s\" with pid %i" %
                 (self.path.name, child.pid))
        self.executable = child
        self.start = time.time_ns()
        # Return self for chaining.
        return self

    def check_status(self):
        "Returns true if the executable has finished execution."
        if self.executable.poll() is not None:
            delta_ms = (time.time_ns() - self.start) / 1000000
            if self.executable.returncode == 0:
                log.warning("Child with pid %i has been executed successfully in %.2f ms!" % (
                    self.executable.pid, delta_ms))
            else:
                log.error("Child with pid %i has stopped execution with code %i." % (
                    self.executable.pid, self.executable.returncode, delta_ms))
            self.done = True
            return True
        else:
            return False

    def do_step(self):
        "Performs one command proccessing step. Returns true if the command finished execution else false."
        # Trying to avoid any potential deadlocks...
        if self.check_status():
            return True
        # Get next command.
        command_text = self.executable.stdout.readline()
        command_stack = cmdsplit(command_text)
        reply = None
        # Parse and execute command.
        if len(command_stack) != 0:
            command = command_stack.pop(0)
            if command in COMMAND_REGISTRY:
                reply = COMMAND_REGISTRY[command](
                    command_stack, self.shadow, self.state)
            else:
                log.warning("Genume: %s: command not found." % (command))
        # Send reply if any.
        if reply is not None:
            self.executable.stdin.write(reply)
            self.executable.stdin.write("\n")
            self.executable.stdin.flush()
        return self.check_status()

    def finish_up(self):
        "Applies all changes to the registry."
        self.root.update(self.shadow)
