import os

APP_LIST_FILE = "list_of_apps.txt"
DASHES = "----------------------"

class GitHandler():
    def __init__(self, workingDirectory):
        self.workingDirectory = workingDirectory
        self.appList = self.generateAppList()
    
    def generateAppList(self):
        appList = None
        
        with open(os.path.join(self.workingDirectory, APP_LIST_FILE)) as f:
            appList = f.readlines()
        
        appList = [x.strip() for x in appList]
            
        return appList
    
    
    def updateRepos(self):
        print("Starting updating of repos...")
        print(DASHES)
        os.chdir(self.workingDirectory + "/../../")
        
        for app in self.appList:
            if (not os.path.isdir(app)):
                print("{} doesn't exit!".format(app))
                continue
            
            os.chdir(os.getcwd() + "/{}/".format(app))
            
            print("Updating {}...".format(app))
            os.system("git pull")
            print("")
            
            os.chdir(os.getcwd() + "/../")
        
        os.chdir(self.workingDirectory)
        return
    
    def cloneRepos(self):
        print("\nStarting cloning of repos...")
        print(DASHES)
        
        os.chdir(self.workingDirectory + "/../../")
        
        for app in self.appList:
            if (os.path.isdir(app)):
                print("{} repository already exists".format(app))
                continue
            
            repoURL = "git@github.com:Student-Technology-Center/{}.git".format(app)
            os.system("git clone {}".format(repoURL))
        
        print("\n")
        os.chdir(self.workingDirectory)
        return
