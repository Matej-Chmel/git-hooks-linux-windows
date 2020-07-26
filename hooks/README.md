# Hooks

This file describes implemented hooks and what they do.

## pre-commit

This hook is fired right after `git commit` command. It's great for modifying files before committing. Among example uses we can find linting, formatting, minifying, etc.

### What does this one do in this example?

#### Version number update (Python)

Before finishing the commit, this hook looks at github page of this repository and reads version number from [version.pydef](../data/version.pydef). Then it updates the local [version.pydef](../data/version.pydef) file and increments version by one.

If an internet connection or `requests` module isn't available it reads the latest version number from local file instead.

## prepare-commit-msg

This hook is fired after `pre-commit` hook completes execution. It's used to format the commit message before saving the commit.

### What does this one do in this example?

#### Prepending version number to commit message (Python)

Because at this stage all files are already in their final form, it can read the right version number from [version.pydef](../data/version.pydef).

First it checks if commit message is already well formatted. If it isn't it prepends a `Version {x}` string to it and saves it.
