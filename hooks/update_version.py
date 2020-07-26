# pylint: disable=import-error
from src.common import data, VERSION

version = None

try:
    from base64 import b64decode
    from requests import get, codes

    token = None

    with data('.token') as file:
        token = file.read()

    URL = (
        'https://api.github.com/repos/Matej-Chmel/'
        'git-hooks-linux-windows/contents/data/version.pydef'
    )

    request = get(URL, headers={'Authorization': f'token {token}'})

    if request.status_code == codes.ok: #pylint: disable=no-member
        print('Reading latest version from github.')
        version = int(b64decode(request.json()['content']))
    else:
        print('Repository or file not found. Reading latest version from local file.')
        version = VERSION

except ImportError:
    print('Module requests not found. Reading latest version from local file.')
    version = VERSION

print(f'Latest version was {version}.')
version += 1

with data('version.pydef', 'w+') as file:
    file.write(str(version))

print(f'Successfully upgraded version to {version}.')
