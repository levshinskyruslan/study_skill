import platform
import sys

info = f'OS info is \n{platform.uname()}\n\nPython version is {sys.version} {platform.architecture()}'

with open('info_system.txt', 'w') as f:
    f.write(info)