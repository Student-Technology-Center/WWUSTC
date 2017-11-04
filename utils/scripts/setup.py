import os
import sys
from subprocess import call
from lib.SystemHandler import getSystem
from lib.GitHandler import GitHandler
from lib.DependencyHandler import installDependencies

SYSTEM_TYPE = getSystem()
WORKING_DIR = os.path.dirname(os.path.realpath(__file__))

def main():
    if (len(sys.argv) < 2):
        throwError("Usage: setup.py <prod | true/false>")
    
    GitHandler(WORKING_DIR).cloneRepos()
    installDependencies(WORKING_DIR)
    
    os.chdir(WORKING_DIR + '/../../')
    
    call('manage.py makemigrations', shell=True)
    call('manage.py migrate', shell=True)
    call('manage.py migrate --run-syncdb', shell=True)
    call('manage.py collectstatic --noinput', shell=True)
    
def throwError(message, shouldExit=True):
    print('Error: {}'.format(message))
    
    if (shouldExit):
        sys.exit(0)
        
if __name__ == '__main__':
    main()
