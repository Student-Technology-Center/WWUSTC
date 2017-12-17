import sys
import os
from subprocess import call
from pylib.SystemHandler import getSystem, SystemType

def main():
    folderName = os.path.relpath(".","..")

    if (folderName != "scripts"):
        print("Please run setup.py inside the scripts folder")
        return

    SYSTEM_TYPE = getSystem()

    WORKING_DIR = os.path.dirname(os.path.realpath(__file__))
    os.chdir(WORKING_DIR + "/subscripts/")

    if (SYSTEM_TYPE == SystemType.WINDOWS):
        call('start_local_dev_server_windows.bat', shell=True)
    elif (SYSTEM_TYPE == SystemType.LINUX):
        call('sh start_local_dev_server_linux.sh', shell=True)

if __name__ == '__main__':
    main()
