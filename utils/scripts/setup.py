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
        throwError("Usage: setup.py <prod | true/false>")
    
    prod = None
    
    if (sys.argv[1] == 'true'):
        prod = True
    elif (sys.argv[1] == 'false'):
        prod = False
    else:
        throwError("Invalid param")
        return
    
    GitHandler(WORKING_DIR).cloneRepos(prod)
    installDependencies(WORKING_DIR)
    
    SYSTEM_TYPE = getSystem()
    
    os.chdir(self.workingDirectory + "/subscripts/")
    
    if (SYSTEM_TYPE == SystemType.WINDOWS):
        call('setup_windows.bat', shell=True)
    elif (SYSTEM_TYPE == SystemType.LINUX):
        call('setup_linux.sh', shell=True)

def throwError(message, shouldExit=True):
    print('Error: {}'.format(message))
    
    if (shouldExit):
        sys.exit(0)
        
if __name__ == '__main__':
    main()
