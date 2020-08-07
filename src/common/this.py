from os.path import abspath, dirname, join, pardir, realpath

REPO_DIR = abspath(join(dirname(realpath(__file__)), pardir, pardir))
DATA_DIR = join(REPO_DIR, 'data')

def data(filename, mode='r'):
    return open(join(DATA_DIR, filename), mode)

def version():
    with data('version.pydef') as file:
        try:
            return int(file.read())
        except:
            return 0
