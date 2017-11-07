import os
import sys
from subprocess import call
from pylib.SystemHandler import getSystem
from pylib.GitHandler import GitHandler
from pylib.DependencyHandler import installDependencies

SYSTEM_TYPE = getSystem()
WORKING_DIR = os.path.dirname(os.path.realpath(__file__))

def main():
    if (len(sys.argv) < 2):
        throwError("Usage: setup.py <prod | true/false>")
    
    GitHandler(WORKING_DIR).cloneRepos()
    installDependencies(WORKING_DIR)
    
def throwError(message, shouldExit=True):
    print('Error: {}'.format(message))
    
    if (shouldExit):
        sys.exit(0)
        
if __name__ == '__main__':
    main()
