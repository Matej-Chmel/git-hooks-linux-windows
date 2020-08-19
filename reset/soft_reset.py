from os import chdir as cd
from os.path import abspath, dirname, join, pardir, realpath
from subprocess import CalledProcessError, check_output as execute
from sys import exit

def command(text, success_message):
	try:
		execute(text.split(' '))
		print(success_message)
	except CalledProcessError as e:
		print(
			f'Something went wrong.\n'
			f'Error code: {e.returncode}\n'
			f'More info: {e.output}\n'
		)
		exit(1)

# Get root directory of this repository.
REPO_DIR = abspath(join(dirname(realpath(__file__)), pardir))

# And move there.
cd(REPO_DIR)

# Remove latest unpushed commit.
command('git reset --soft HEAD~1', 'Latest unpushed commit removed.')

# Remove staged changes.
command('git reset HEAD -- .', 'Staged changes removed.')

print('Soft reset completed.')
