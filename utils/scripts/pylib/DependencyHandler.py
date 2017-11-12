import pip
import os

def installDependencies(workingDirectory):
    fileName = "list_of_python_dependencies.txt"
    
    dependenciesList = None
        
    with open(os.path.join(workingDirectory, fileName)) as f:
        dependenciesList = f.readlines()
    
    dependenciesList = [x.strip() for x in dependenciesList]
    
    for dependency in dependenciesList:
        pip.main(['install', dependency])
    
    installLfpPw(workingDirectory)

def installLfpPw(workingDirectory):
    os.chdir(workingDirectory + "/../../")
    
    lfpDirPath = "{}\lfp_scheduler".format(os.getcwd())
    
    if (not os.path.isdir(lfpDirPath)):
        print("lfp_scheduler directory not found!")
        return
    
    os.chdir(lfpDirPath)
    
    if (not os.path.isfile("lfp_pw.py")):
        print("Creating lfp_pw.py")
        os.system("echo LFP_CLIENT_ID='' >> lfp_pw.py")
        os.system("echo LFP_CLIENT_SECRET='' >> lfp_pw.py")
    
    os.chdir(workingDirectory)
