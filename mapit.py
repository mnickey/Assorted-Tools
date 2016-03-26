#! python2.7
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.

import webbrowser
import sys
import pyperclip


if len(sys.argv) > 1:
    # Get the address from the command line
    address = ' '.join(sys.argv[1:])
else:
    # Get the address from the clipboard
    address = pyperclip.paste()

webbrowser.open("https://www.google.com/maps/place/" + address)
