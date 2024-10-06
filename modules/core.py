import json
import os
import sys
DataBase='data/PPT.json'

def newfile(fileName):
    with open(DataBase,"w") as wf:
        json.dump(fileName,wf,indent=4)
        
def readFile():
    with open(DataBase, "r") as rf:
        return json.loas(rf)

def addData(dicName):
    with open(DataBase, "w") as frw:
        json.dumb(dicName,frw, indent=4)
        
def checkFile(dicName):
    if (os.path.isfile(DataBase)):
        pass
    else:
            newfile(dicName)
            
        