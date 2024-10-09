import json
import os
def saveData(data, filename='data/puntajes.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)# indent=4 hace que el JSON sea más legible al agregar sangrías.

def updateData(filename='data/puntajes.json'):
    if not os.path.exists(filename):
         # Si no existe, crea un nuevo archivo y escribe un diccionario vacío en él
        with open(filename, 'w') as f: #carga el contenido en modo escritura
            json.dump({}, f)
        return {} #devuelvo el diccionario vacio
    else:
        with open(filename, 'r') as f:  # Si el archivo existe, lo abre en modo lectura
            return json.load(f)# Carga el contenido del archivo y lo devuelve como un diccionario
        
