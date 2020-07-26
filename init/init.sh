#!/bin/bash

# Run this script right after cloning the repository.
# Suitable for Linux.

# Introduce this script.
echo init.sh called

# Let's move into the root directory of this repository.
cd $(dirname "$(readlink -f "$0")")/..

# Tell git to look for hooks in our custom hooks directory.
git config core.hooksPath hooks

# Check exit code of the last call and print the result.
if [[ $? == 0 ]]; then
    echo Hooks were configured successfully.
else
    echo Something went wrong.
    exit 1
fi

# Check that we are on Linux. If we are not, our job is completed.
if [[ $OSTYPE != linux* ]]; then
    exit 0
fi

# Linux requires execute permissions for hooks, so we'll grant them.

# Move into hooks directory.
cd hooks

# Grant x permission to each file without extension.
for file in *; do
    case $file in *.*) continue;; esac
    chmod +x $file
    echo Permission granted to $file.
done

# Check if everything went fine.
if [[ $? == 0 ]]; then
    echo Permissions were granted to all hooks successfully.
else
    echo Something went wrong.
    exit 1
fi
