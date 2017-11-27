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

    if (len(sys.argv) < 2):
        throwError("Usage: setup.py <prod | dev | local> (timeout)")
    
    settings = None
    
    if (sys.argv[1] == 'prod'):
        settings = "settings"
    elif (sys.argv[1] == 'dev'):
        settings = "dev-settings"
    elif (sys.argv[1] == 'local'):
        prod = False
        settings = "local-dev-settings"
    else:
        throwError("Invalid param")
        return
    
    timeout = 0
    if (len(sys.argv) > 2):
        timeout = int(sys.argv[2])

    SYSTEM_TYPE = getSystem()
    WORKING_DIR = os.path.dirname(os.path.realpath(__file__))
    gitHandler = GitHandler(WORKING_DIR)

    update(SYSTEM_TYPE, WORKING_DIR, gitHandler, timeout, settings)

def update(SYSTEM_TYPE, WORKING_DIR, gitHandler, timeout, settings):
    if (SYSTEM_TYPE == SystemType.WINDOWS):
        #gitHandler.updateRepos()
        os.chdir(WORKING_DIR + "/subscripts/")
        call('update_windows.bat ' + settings, shell=True)
    elif (SYSTEM_TYPE == SystemType.LINUX):
        gitHandler.updateRepos()
        os.chdir(WORKING_DIR + "/subscripts/")
        call('sh update_linux.sh ' + settings, shell=True)

    if (timeout == 0):
        return
    sleep(timeout / 1000.0)

    update(SYSTEM_TYPE, WORKING_DIR, gitHandler, timeout, settings)

def throwError(message, shouldExit=True):
    print('Error: {}'.format(message))

    if (shouldExit):
        sys.exit(0)

if __name__ == '__main__':
    main()
