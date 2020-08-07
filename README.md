# Git hooks for both Linux and Windows
Example repository that shows how to integrate git hooks when switching between Linux and Windows platforms.

## What are git hooks?
Git hooks are scripts that are triggered by certain git commands like `git commit` or `git push`. These can then do a lot of exhausting work for you.

## Examples of use
- enforce code standards
- format code
- format commit message
- linting
- minifying
- etc.

## Try it yourself
The current setup implements two hooks. One changes version number on each commit, the other formats commit message.

1. Fork the repo.
2. Init the repo. Go to [init](init/) directory and read more.
3. Enter your username and repository name in [repo.pydef](data/repo.pydef) file.
4. If your newly forked repository is private, read something about [tokens](data/).
5. Write something to the [chat](data/chat.txt) file so that git detects a change.
6. Write a commit message, commit and push.
7. Your commit message should be changed by the hook and [version number](data/version.pydef) should increase.

## What programming languages are required?
Git hooks can be written in any language but the first line of a hook file has to tell what language it's written in with the `#!`. However not all systems recognize this and they run the hook in their own shell.

If you want to write truly cross-platform hooks, I recommend writing one-line hook scripts that execute other files about which you know they work on all your machines.

A great example is the [pre-commit](hooks/pre-commit) hook that executes a Python script.

## What git client is necessary?
Any. I use GitHub Desktop on one of my machines (arguably the most limited version) and it works just fine.

## What's next?
Look at the [hooks](hooks/). Each script contains comments that should help you learn something about git hooks and how they work.

When you start to understand how to use them, you can utilize them in your own projects.
