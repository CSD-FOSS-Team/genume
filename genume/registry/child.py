from shlex import split as cmdsplit
import subprocess as sbpr
import logging as log
import time
import os

from genume.constants import VERSION, NAME, DESC, SCRIPTS_BASH_EXTRA
from genume.utils import merge_dicts, find_key_of_value
from genume.registry.category import CategoryEntry
from genume.registry.parser import COMMAND_REGISTRY


class ChildHandler:
    """Handles child lifecycle and command parsing."""

    def __init__(self, path, root_cat, parent):
        self.path = path
        self.root = root_cat
        self.shadow = CategoryEntry()
        self.state = {}
        self.observer = parent.observer
        self.done = False

    def generate_env(self):
        "Generates the environment variables that are passed to the child"
        name = "root"
        if self.root.parent is not None:
            name = find_key_of_value(root.parent, root)
        extra_env = {"HOST_VERSION": VERSION, "HOST_NAME": NAME,
                     "HOST_DESC": DESC, "MASTER_CATEGORY": name}
        env = merge_dicts(extra_env, os.environ)
        # Generate new path.
        env["PATH"] = SCRIPTS_BASH_EXTRA + ":" + env["PATH"]
        return env

    def start(self):
        "Prepares and launches the child."
        child = sbpr.Popen(args=str(self.path), shell=False, bufsize=0, universal_newlines=True,
                           stdin=sbpr.PIPE, stdout=sbpr.PIPE, close_fds=False, env=self.generate_env())
        log.debug("Started child \"%s\" with pid %i" %
                  (self.path.name, child.pid))
        self.executable = child
        self.start = time.time_ns()
        # Return self for chaining support.
        return self

    def check_status(self):
        "Returns true if the executable has finished execution."
        if self.executable.poll() is not None:
            delta_ms = (time.time_ns() - self.start) / 1000000
            if self.executable.returncode == 0:
                log.info("Child %s (%i) has been executed successfully in %.2f ms!" % (
                    self.path.name, self.executable.pid, delta_ms))
            else:
                log.error("Child %s (%i) has stopped execution with code %i." % (
                    self.path.name, self.executable.pid, self.executable.returncode, delta_ms))
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
                parse_func = COMMAND_REGISTRY[command]
                reply = parse_func(command_stack, self.shadow, self.observer, self.state)
            else:
                log.warning("%s: command not found." % (command))
        # Send reply if any.
        if reply is not None:
            self.executable.stdin.write(reply)
            self.executable.stdin.write("\n")
            self.executable.stdin.flush()
        return self.check_status()

    def finish_up(self):
        "Applies all changes to the registry."
        self.root.merge(self.shadow)
