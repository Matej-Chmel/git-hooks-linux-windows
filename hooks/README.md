# Hooks

This file describes implemented hooks and what they do.

## pre-commit

This hook is fired right after `git commit` command. It's great for modifying files before committing. Among example uses we can find linting, formatting, minifying, etc.

### What does this one do in this example?

#### Version number update (Python)

Before finishing the commit, this hook looks at the GitHub page of this repository and reads version number from [version.pydef](../data/version.pydef). Then it updates the local version.pydef file and increments version by one.

> Warning: To access GitHub API, this hook uses 'requests' module. If you don't have it installed, you can do so by running 'python -m pip install requests --user' or equivalent for your environment.

If a problem occurs, it reads the latest version number from local file instead.

## prepare-commit-msg

This hook is fired after the `pre-commit` hook completes execution. It's used to format the commit message before saving the commit.

### What does this one do in this example?

#### Prepending version number to commit message (Python)

Because at this stage all files are already in their final form, it can read the right version number from [version.pydef](../data/version.pydef).

This hook enforces following commit message format:

```
Version {version_number}. {message}
```

First it checks if commit message is already well formatted. If it isn't, it prepends a `Version {version_number}.` string to it and saves it.
