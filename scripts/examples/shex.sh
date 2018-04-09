#!/bin/bash
if [ -z "$GENUME_VERSION" ]; then
    echo "Running outside of enumeration."
else
    # The first echo command outputs to stderr which does not get read by the registry.
    >&2 echo -e "Running within ${GENUME_VERSION} genume version."
    echo -e "KVAL test \"I am a test string.\""
fi