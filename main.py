import os
import sys
import modules as modulo
from modules.jsonM import updateData, saveData


if __name__ == '__main__':
    isActive = True
    
    while isActive:
        try:
            print(modulo.menu)#imprimimos el menu desde el modulo menu, donde tenemos toda la info de este
            opcion = int(input('Escriba aquí la opción: ')) 
        
            match opcion:
                case 1:
                    
                    datos = updateData()# Carga los datos desde el archivo JSON
                    datos_actualizados = modulo.jugarPc(datos)# Inicia el juego y obtiene los datos actualizados
                    saveData(datos_actualizados)# Guarda los datos actualizados en el archivo JSON
                case 2:
                    datos = updateData()
                    datos_actualizados = modulo.jugarJug(datos)
                    saveData(datos_actualizados)
                case 3:
                    print(modulo.reglas)# Imprime las reglas importadas desde el módulo
                    input('Enter para volver al menú.....')
                    modulo.borrar_pantalla()
                case 4:
                    print("Saliendo del juego...")
                    isActive = False# Cambia la variable para terminar el bucle
                case _:
                    print("Opción no válida. Por favor, elija una opción correcta.")
        except ValueError:
            input('Elija una opción correcta. Presione Enter para continuar...')

    print("¡Gracias por jugar!")