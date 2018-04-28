import os
import sys
from subprocess import call
from pylib.SystemHandler import getSystem, SystemType
from pylib.GitHandler import GitHandler
from pylib.DependencyHandler import installDependencies

WORKING_DIR = os.path.dirname(os.path.realpath(__file__))

def main():
    folderName = os.path.relpath(".","..")
    if (folderName != "scripts"):
        print("Please run setup.py inside the scripts folder")
        return

    if (len(sys.argv) < 2):
        throwError("Usage: setup.py <prod | dev | local>")

    prod = None
    settings = None

    if (sys.argv[1] == 'prod'):
        prod = True
        settings = "settings"
    elif (sys.argv[1] == 'dev'):
        prod = False
        settings = "dev-settings"

    #This nmight be temporary
    elif (sys.argv[1] == 'local'):
        prod = False
        settings = "dev-settings"
    else:
        throwError("Invalid param")
        return

    GitHandler(WORKING_DIR, prod).cloneRepos()
    installDependencies(WORKING_DIR)

    SYSTEM_TYPE = getSystem()
    os.chdir(WORKING_DIR + "/subscripts/")

    if (SYSTEM_TYPE == SystemType.WINDOWS):
        call('setup_windows.bat ' + settings, shell=True)
    elif (SYSTEM_TYPE == SystemType.LINUX):
        call('sh setup_linux.sh ' + settings, shell=True)

def throwError(message, shouldExit=True):
    print('Error: {}'.format(message))

    if (shouldExit):
        sys.exit(0)

if __name__ == '__main__':
    main()
