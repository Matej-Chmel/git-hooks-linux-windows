# What should I do to setup this repository?
Based on your OS and environment choose one script in this directory and run it.

## What does the script do?
- The script tells git to look for hooks in the [hooks](../hooks/) directory.
- On Linux it grants execute permission to all the shell scripts in [hooks](../hooks/) directory.

## What do I need to run it?
It's highly probable that you can already run at least one of the scripts without installing anything extra. For example, on Windows I bet you can run Batch files.

## Where do I run it?

It does not matter from where you run the script. If it's not moved, it should find the root directory of this repository and successfully setup hooks.

## Examples

### Windows
#### Batch
```
init\init.bat
```

#### Python launcher
```
py init/init.py
```

### Linux
#### Bash
```
bash init/init.sh
```

#### Python
```
python init/init.py
```
