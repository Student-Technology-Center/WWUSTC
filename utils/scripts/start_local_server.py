from multiprocessing import Process
import os
import subprocess

def main():
    print("Beginning Django server")

    #Begins the server process
    p = Process(target=launcher_server)
    p.start()
    p.join()

def launcher_server():

    py_commands = [
        'py',
        'python',
        'python3'
    ]

    os.chdir('../../')

    for cmd in py_commands:
        subprocess.call('{} manage.py runserver --settings=wwustc.local-dev-settings'.format(cmd), shell=True)

if __name__ == '__main__':
    main()
