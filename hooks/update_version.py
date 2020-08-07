# pylint: disable=import-error
from ast import literal_eval as eval
from src.common import data, version

def latest_version():
    '''Returns the latest version number or None if a problem occurs.'''
    try:
        # Try reading the repository from GitHub.
        # Request module is required.
        from base64 import b64decode
        from requests import get, codes

        repo_name = None
        request = None
        token = None
        user = None

        # Read local information about the repository.
        try:
            with data('repo.pydef') as file:
                repo: dict = eval(file.read())
                user = repo['user']
                repo_name = repo['name']
        except OSError:
            return print('File repo.pydef not found.')
        except:
            return print('Trouble parsing repo dictionary.')

        # Try to read local token.
        # Token is necessarry if the repository is private.
        try:
            with data('.token') as file:
                token = file.read().rstrip('\n')
        except OSError:
            print('Token not present. Assuming that the repository is public.')
        
        # Build url and send request through GitHub API.
        url = (
            'https://api.github.com/repos/'
            f'{user}/{repo_name}/'
            'contents/data/version.pydef'
        )

        if token is None:
            # Assume that repository is public. No header needed.
            request = get(url)
        else:
            # Token is available. Send it inside the Authorization header.
            request = get(url, headers={'Authorization': f'token {token}'})
        
        if request.status_code == codes.ok: #pylint: disable=no-member
            print('Reading latest version from github.')
            # Before we can read the content, we have to decode it.
            return int(b64decode(request.json()['content']))
        else:
            return print('Repository or file not found.')
        
    except ImportError:
        return print("Module 'requests' not found.")

# First read the latest version number.
latest = latest_version()

if latest is None:
    # Problem occured. Read the version number from data/version.pydef file.
    print('Reading latest version from local file.')
    latest = version()

print(f'Latest version was {latest}.')
latest += 1

with data('version.pydef', 'w+') as file:
    file.write(str(latest))

print(f'Successfully upgraded version to {latest}.')
