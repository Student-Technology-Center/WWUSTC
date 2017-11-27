import os
import sys
from subprocess import call
from pylib.SystemHandler import getSystem, SystemType
from pylib.GitHandler import GitHandler
from time import sleep

def main():
    folderName = os.path.relpath(".","..")

    if (folderName != "scripts"):
        print("Please run update.py inside the scripts folder")
        return

    timeout = 0
    if (len(sys.argv) > 1):
        timeout = int(sys.argv[1])

    SYSTEM_TYPE = getSystem()
    WORKING_DIR = os.path.dirname(os.path.realpath(__file__))
    gitHandler = GitHandler(WORKING_DIR)

    update(SYSTEM_TYPE, WORKING_DIR, gitHandler, timeout)

def update(SYSTEM_TYPE, WORKING_DIR, gitHandler, timeout):
    if (SYSTEM_TYPE == SystemType.WINDOWS):
        gitHandler.updateRepos()
        os.chdir(WORKING_DIR + "/subscripts/")
        call('update_windows.bat', shell=True)
    elif (SYSTEM_TYPE == SystemType.LINUX):
        gitHandler.updateRepos()
        os.chdir(WORKING_DIR + "/subscripts/")
        call('sh update_linux.sh', shell=True)

    if (timeout == 0):
        return
    sleep(timeout / 1000.0)

    update(SYSTEM_TYPE, WORKING_DIR, gitHandler, timeout)

if __name__ == '__main__':
    main()
