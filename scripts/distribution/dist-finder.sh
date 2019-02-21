#!/bin/sh

# Fullproof way of finding the user's preferences=distribution.
# Posix shell compliant.

configure cat sed tr uname
# The currently correct way.
releasefile() {
    if [ -f "/etc/os-release" ]; then
        # Load variables from file.
        . /etc/os-release
        DISPLAY_NAME="${NAME} ${VERSION}"
        EXTRA_URL="${HOME_URL}"
        return 0
    else
        # Not available.
        return 1
    fi
}

# Another correct way.
issue() {
    if [ -f "/etc/issue" ]; then
        # Needs more testing because of the special formatting options /etc/issue has.
        DISPLAY_NAME=$(cat /etc/issue | sed -e 's/\\[nl]//g' | tr '\n' ' ' | sed -e 's/[ \t]*$//')
        return 0
    else
        # Not available.
        return 1
    fi
}

# The previous correct way.
lsbrel() {
    command -v lsb_release
    if [ $? -eq 0 ]; then
        # If it fails then the variable is not set.
        DISPLAY_NAME=$(lsb_release -vs | tr '\n' ' ')
        return 0
    else
        # Not available.
        return 1
    fi
}

# Give up.
giveup() {
    # I said foolproof not always correct.
    DISPLAY_NAME="Unknown"
}

# Globals.
DISPLAY_NAME=""
EXTRA_URL=""
LINUX_INFO=""

# Main.
releasefile
if [ $? -ne 0 ]; then
    issue
    if [ $? -ne 0 ]; then
        lsbrel
    fi
fi
if [ -z "$DISPLAY_NAME" ]; then
    giveup
fi
# Get linux version.
ARCH=$(uname -m)
LINUX_VERSION=$(uname -sr)
LINUX_INFO="${LINUX_VERSION}(${ARCH})"
# Output findings.
value dist_name "${DISPLAY_NAME}"
if [ ! -z "$EXTRA_URL" ]; then
    value dist_url "${EXTRA_URL}"
fi
value kernel "${LINUX_INFO}"

