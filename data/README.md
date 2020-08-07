# GitHub integration
When working with a team, you want the progress to be shared safely without any conflicts. To do this, the hooks have to access GitHub page of your repository and check some important things before you commit.

## Public repository
If your repository is public. You can skip the rest of this file and live a happy life.

## Private repository
To allow your hooks to reach GitHub page of your repository, follow these steps:

1. Log into your GitHub account.
2. Go to https://github.com/settings/tokens
    - If the link doesn't work, try this:
        - Go to github.com
        - Click on your profile picture in top right corner.
        - Choose `Settings`.
        - Choose `Developer settings` from the left panel. It's the last option at the bottom.
        - Choose `Personal access tokens` from the left panel.
3. Click on `Generate new token` from the right side.
4. Enter your password.
5. Name your token in the `Note` textbox.
6. Tick `repo` scope.
7. Confirm by clicking on `Generate token` at the bottom of the page.
8. Copy the generated token.
9. Create file named `.token` in the data directory (directory of this file).
10. Paste the token into the file and save the file.

### Is it safe to have a token in a repository?
If a token is in the repository, it should be ignored by [.gitignore](../.gitignore). Notice that current .gitignore file already does so.

> Do not share your token with anyone.

### How to use the token?
When accessing GitHub page of your repository from a hook script, you have to send an `Authorization` header with the token inside the request. A working example can be found in [update_version.py](../hooks/update_version.py), line 49.
