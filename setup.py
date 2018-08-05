import os
import sys
from git import Repo, GitCommandError
from subprocess import check_call

def main():
    """Handles first time setup of wwustc server

    Does the following:
    - Clone Repos
    - Configure LFP Scheduler
    - Pip install requirments
    - Migrate and collect static
    """

    # True if no extra param was given
    if len(sys.argv) < 2:
        print("Usage: setup.py <prod | dev>")

    param = sys.argv[1]
    isProd = False
    if param == "prod":
        isProd = True
    elif param != "dev":
        # "prod" or "dev" must be given
        print("Error: Invalid Param")
        return

    # Get path of this file
    basePath = os.path.dirname(os.path.abspath(__file__))

    # Begin cloning repos
    clone_repos(basePath, isProd)

    # True if lfp_scheduler repo exists
    # Handles setting up lfp scheduler
    if os.path.isdir(os.path.join(basePath, "lfp_scheduler")):
        handle_lfp_scheduler(basePath)

    # pip install requirements from requirements.txt
    install_pip_requirements(basePath)

    # Migrate and collect static for django
    migrate_and_collect_static(basePath, isProd)

def install_pip_requirements(basePath):
    """Installs pip requirements
    """
    # Get file path
    requirementPath = os.path.join(basePath, "requirements.txt")

    # Construct argument template
    argList = [sys.executable, "-m", "pip", "install", ""]

    with open(requirementPath, "r") as requirements:
        # Read the requirements
        for req in requirements.readlines():
            # Attempt to install requirement
            argList[-1] = req.rstrip()
            try:
                check_call(argList)
            except: pass


def handle_lfp_scheduler(basePath):
    """Configures lfp scheduler
    
    lfp_scheduler won't work without a lfp_pw password file, generate it here
    if missing
    """

    # Get path of repo
    lfpSchedulerPath = os.path.join(basePath, "lfp_scheduler")

    # Print warning and return if no folder
    if not os.path.isdir(lfpSchedulerPath):
        print("Warning! lfp_scheduler repo not found")
        return
    
    # Path to file
    lfpFilePath = os.path.join(lfpSchedulerPath, "lfp_pw.py")
    
    # True if file doesnt exist
    if not os.path.isfile(lfpFilePath):
        print("Lfp pw file doesn't exist, creating...")
        # Create file
        with open(lfpFilePath, 'w+') as f:
            f.write("LFP_CLIENT_ID=''\n")
            f.write("LFP_CLIENT_SECRET=''\n")

def migrate_and_collect_static(basePath, isProd):

    settingsParam = "--settings=wwustc."
    if isProd:
        settingsParam += "settings"
    else:
        settingsParam += "dev-settings"
    
    check_call([sys.executable, "manage.py", "makemigrations", settingsParam])
    check_call([sys.executable, "manage.py", "migrate", settingsParam])
    check_call([sys.executable, "manage.py", "migrate", "--run-syncdb", settingsParam])
    check_call([sys.executable, "manage.py", "collectstatic", "--noinput", settingsParam])


def clone_repos(basePath, isProd):
    """Clones all app repos

    Iterates over apps.txt and clones all repos that are missing
    """
    print("\nStarting clones of repos...")
    print("----------------------")

    branchName = "prod" if isProd else "master"
    baserepo = "git@github.com:Student-Technology-Center/"

    with open("apps.txt", 'r') as appList:
        # Begin iterating over apps
        for app in appList.readlines():
            # Strip new line and whitespace
            app = app.rstrip()
            # Create path to repo
            appPath = os.path.join(basePath, app)
            
            # True if repo exists
            if os.path.isdir(appPath):
                print("%s already exists, skipping..." % app)
                continue
            
            # Make the folder for the app
            os.makedirs(app)
            # Try cloning
            try:
                Repo.clone_from(baserepo + app + ".git", appPath, branch=branchName)
                print("Succesfully cloned %s" % app)
            except GitCommandError:
                # Exception occurs when branch doesnt exist, warn user, delete folder, and continue
                print("Repo %s does not have a %s branch, skipping..." % (app, branchName))
                os.rmdir(appPath)


if __name__ == "__main__":
    main()
