#pylint: disable=import-error
import re
from sys import argv
from src.common import VERSION

message = None

# argv[1] is the path to the file that contains the commit message.

with open(argv[1], 'r') as file:
    message = file.read()

if re.match(r'^Version\s\d+\.\s[^\s]((.|\n)*)$', message) is None:
    # Message is not formatted correctly.
    # Let's prepend version string to the message.
    message = f'Version {VERSION}. {message}'
    print(f"Formatted message to '{message}'")
else:
    print('Message was formatted fine.')

# Now we have to save the message back to the file.

with open(argv[1], 'w') as file:
    file.write(message)
