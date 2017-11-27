import pip
import os

def installDependencies(workingDirectory):
    fileName = "list_of_python_dependencies.txt"
    
    dependenciesList = None
    
    # We first make a list of all dependencies
    with open(fileName) as f:
        dependenciesList = f.readlines()
    
    # Strip whitespace and special characters
    dependenciesList = [x.strip() for x in dependenciesList]
    
    # Attempt to install the dependencies
    for dependency in dependenciesList:
        pip.main(['install', dependency])
    
    installLfpPw(workingDirectory)

def installLfpPw(workingDirectory):
    os.chdir(workingDirectory + "/../../")
    
    if (not os.path.isdir('lfp_scheduler')):
        print("lfp_scheduler directory not found!")
        return
    
    os.chdir(os.getcwd() + "/lfp_scheduler/")
    
    if (not os.path.isfile("lfp_pw.py")):
        print("Creating lfp_pw.py")
        f = open("lfp_pw.py", "w+")
        f.write("LFP_CLIENT_ID=''\n")
        f.write("LFP_CLIENT_SECRET=''\n")
    
    os.chdir(workingDirectory)
