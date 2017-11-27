import os

APP_LIST_FILE = "list_of_apps.txt"
DASHES = "----------------------"

class GitHandler():
    def __init__(self, workingDirectory):
        self.workingDirectory = workingDirectory
        self.appList = self.generateAppList()
   
    # Opens a txt file and creates a python list of strings for each line
    # This is used to iterate through later
    def generateAppList(self):
        appList = None
        
        with open(os.path.join(self.workingDirectory, APP_LIST_FILE)) as f:
            appList = f.readlines()
        
        appList = [x.strip() for x in appList]
            
        return appList
    
    
    def updateRepos(self):
        print("Starting updating of repos...")
        print(DASHES)
        # We first move up 2 folders
        os.chdir(self.workingDirectory + "/../../")
        
        print("Updating wwustc...")
        os.system("git pull")
        
        # Iterate through our custom list and assure every folder exists
        for app in self.appList:
            # If the folder doesn't exist we note it and continue
            if (not os.path.isdir(app)):
                print("{} doesn't exit!".format(app))
                continue
            
            # If the folder does exist, we move into it
            os.chdir(os.getcwd() + "/{}/".format(app))
            
            print("Updating {}...".format(app))
            # Git pull to update
            os.system("git pull")
            print("")
            
            # We go back up
            os.chdir(os.getcwd() + "/../")
        
        # We always make sure to go back
        os.chdir(self.workingDirectory)
        return
    
    # Used in setup.py
    def cloneRepos(self, prod):
        print("\nStarting cloning of repos...")
        print(DASHES)
        
        os.chdir(self.workingDirectory + "/../../")
        
        branch = 'prod' if prod else 'master'
        
        # Similar as updateRepos, we iterate through each app and if it doesnt exist, we clone it
        for app in self.appList:
            if (os.path.isdir(app)):
                print("{} repository already exists".format(app))
                continue
            
            
            # Clone the ssh version of our repos
            repoURL = "git@github.com:Student-Technology-Center/{}.git".format(app)
            print("git clone -b {} {}".format(branch, repoURL))
            os.system("git clone -b {} {}".format(branch, repoURL))
        
        print("\n")
        # We always make sure to go back
        os.chdir(self.workingDirectory)
        return
