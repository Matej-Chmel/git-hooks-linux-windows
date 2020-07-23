#!/bin/sh

# Run this script right after cloning the repository.
# Suitable for Linux.

# Introduce this script.
echo init.sh called

# Let's move into the root directory of this repository.
cd $(dirname "$(readlink -f "$0")")/..

# Let's tell git to look for hooks in our custom hooks directory.
git config core.hooksPath hooks

# Check exit code of the last call and print the result.
if [[ $? == 0 ]]; then
    echo Hooks were configured successfully.
else
    echo Something went wrong.
fi
