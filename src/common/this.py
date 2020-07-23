from os.path import abspath, dirname, join, pardir, realpath

REPO_DIR = abspath(join(dirname(realpath(__file__)), pardir, pardir))
DATA_DIR = join(REPO_DIR, 'data')
VERSION = None

def confirm(prompt):
    while True:
        answer = input(f'{prompt} (y/n): ')
        if answer in ['y', 'yes', 'ok']:
            return True
        if answer in ['n', 'no', 'nope']:
            return False
        print('Please answer yes or no.')

def data(filename, mode='r'):
    return open(join(DATA_DIR, filename), mode)

with data('version.pydef') as file:
    try:
        VERSION = int(file.read())
    except:
        VERSION = 0
