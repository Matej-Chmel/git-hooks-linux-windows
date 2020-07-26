#!/bin/bash

# Move into root directory of this repository.
cd $(dirname "$(readlink -f "$0")")/..

# Remove latest unpushed commit.
git reset --soft HEAD

# Remove staged changes.
git reset HEAD -- .

# Check results.
if [[ $? == 0 ]]; then
    echo Soft reset completed.
else
    echo Something went wrong.
    exit 1
fi
