
import os
import sys
import time
from git.cmd import Git
from subprocess import check_call


def main():
    # True if second param was not passed
    if len(sys.argv) < 2:
        print("Usage: setup.py <prod | dev> (timeout)")
        return
    
    param = sys.argv[1]

    # Set if prod and specify settings
    isProd = False
    settingsParam = "--settings=wwustc."
    if param == "prod":
        isProd = True
        settingsParam += "settings"
    elif param == "dev":
        settingsParam += "dev-settings"
    else:
        print("Error: Invalid Param")
        return
    
    # Get path of this file
    basePath = os.path.dirname(os.path.abspath(__file__))

    # Get optional timeout value from command line
    # otherwise 0
    timeout = int(sys.argv[2]) if len(sys.argv) == 3 else 0

    # Iterate over each app and create a tuple containing the Git object of the
    # repo and then the repo's name
    appList = [(Git(basePath), "wwustc")]
    with open("apps.txt", "r") as appTxt:
        for app in appTxt.readlines():
            app = app.rstrip()
            appPath = os.path.join(basePath, app)
            if os.path.isdir(appPath):
                appList.append((Git(appPath), app))

    # If timeout is 0, update and migrate
    if timeout == 0:
        update_repos(basePath, appList)
        migrate(basePath, settingsParam)
        # Collect static if on prod
        if isProd:
            collect_static(basePath, settingsParam)
    # Otherwise we run on a loop
    # Prod collects static while dev does not
    elif isProd:
        while True:
            update_repos(basePath, appList)
            migrate(basePath, settingsParam)
            collect_static(basePath, settingsParam)
            print("Sleeping for %d seconds\n" % timeout)
            time.sleep(timeout)
    else:
        while True:
            update_repos(basePath, appList)
            migrate(basePath, settingsParam)
            print("Sleeping for %d seconds\n" % timeout)
            time.sleep(timeout)
    

def update_repos(basePath, appList):
    """Updates repos
    """
    # Iterate over each git object and repo and updates
    for appRepo, appName in appList:
        print("Updating %s..." % appName)
        print(appRepo.pull())
        print("--------------------\n")


def migrate(basePath, settingsParam):
    """Perform migrations
    """
    print("Migrating...")
    try:
        check_call([sys.executable, "manage.py", "makemigrations", settingsParam])
        check_call([sys.executable, "manage.py", "migrate", settingsParam])
    except: pass


def collect_static(basePath, settingsParam):
    """Collects static
    """
    print("Collecting static...")
    try:
        check_call([sys.executable, "manage.py", "collectstatic", "--noinput", settingsParam])
    except: pass


if __name__ == "__main__":
    main()
