# TODO: implement


def parse_conf(stack, root, state):
    pass


def parse_set(stack, root, state):
    pass


def parse_value(stack, root, state):
    pass


def parse_subcat(stack, root, state):
    pass


COMMAND_REGISTRY = {
    "CONF": parse_conf, "SET": parse_set,
    "VALUE": parse_value, "SUBCAT": parse_subcat
}
