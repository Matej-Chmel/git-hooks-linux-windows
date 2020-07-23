# Run this script right after cloning the repository.
# Suitable for any OS with Python installed.

# This could be done using the git module. But why bother installing it.
from os import chdir as cd
from os.path import abspath, dirname, join, pardir, realpath
from subprocess import CalledProcessError, check_output as execute

# Introduce ourselves.
print('init.py called')

# Get root directory of this repository.
REPO_DIR = abspath(join(dirname(realpath(__file__)), pardir))

# And move there.
cd(REPO_DIR)

# Let's tell git to look for hooks in our custom hooks directory.
# If something goes wrong, abort and tell user about it.
try:
    execute(['git', 'config', 'core.hooksPath', 'hooks'])
    print('Hooks were configured successfully.')
except CalledProcessError as e:
    print(
        f'Something went wrong.\n'
        f'Error code: {e.returncode}\n'
    )
