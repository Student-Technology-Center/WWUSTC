import os
import sys
from subprocess import call
from lib.SystemHandler import getSystem
from lib.GitHandler import GitHandler
from time import sleep

SYSTEM_TYPE = getSystem()
WORKING_DIR = os.path.dirname(os.path.realpath(__file__))

def main():
    timeout = 0
    
    if (len(sys.argv) > 1):
        timeout = int(sys.argv[1])

    gitHandler = GitHandler(WORKING_DIR)
    
    while(True):
        gitHandler.updateRepos()
        
        os.chdir(WORKING_DIR + '/../../')
        
        call('manage.py makemigrations', shell=True)
        call('manage.py migrate', shell=True)
        call('manage.py collectstatic --noinput', shell=True)
        
        os.chdir(WORKING_DIR)
        
        if (timeout == 0):
            break;
        
        sleep(timeout / 1000.0)
        
if __name__ == '__main__':
    main()
