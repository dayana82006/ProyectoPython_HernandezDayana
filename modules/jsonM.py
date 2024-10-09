import json
import os
def saveData(data, filename='data/puntajes.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def updateData(filename='data/puntajes.json'):
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            json.dump({}, f)
        return {}
    else:
        with open(filename, 'r') as f:
            return json.load(f)
        
