import json
import os
DATA='data/tablaPuntos.json'

def newFile(fileName):
    with open(DATA,"w") as wf:
        json.dump(fileName, wf , indent=4)
        
def readFile():
    with open(DATA, "r") as rf:
        return json.load(rf)
    
def addData(diccName):
    with open(DATA, "w") as frw:
        json.dump(diccName, frw, indent=4)
        
def checkFile(diccName):
    if(os.path.isfile(DATA)):
        pass
    else:
        newFile(diccName)