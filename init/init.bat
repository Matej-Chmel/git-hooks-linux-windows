rem Run this script right after forking the repository.
rem Suitable for Windows.

rem Introduce this script.
echo init.bat called

rem Figure out this script's directory.
set script_dir=%~dp0
set script_dir=%script_dir:~0, -1%

rem Let's move into the root directory of this repository.
cd %script_dir%\..

rem Let's tell git to look for hooks in our custom hooks directory.
git config core.hooksPath hooks

rem Check exit code of the last call and print the result.
if %errorlevel% == 0 (
    echo Hooks were configured successfully.
) else echo Something went wrong.
