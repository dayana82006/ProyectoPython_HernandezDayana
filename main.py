import os
import sys
import modules as modulo
from modules.jsonM import updateData, saveData


if __name__ == '__main__':
    isActive = True
    
    while isActive:
        try:
            print(modulo.menu)
            opcion = int(input('Escriba aquí la opción: '))
        
            match opcion:
                case 1:
                    
                    datos = updateData()
                    datos_actualizados = modulo.jugarPc(datos)
                    saveData(datos_actualizados)
                case 2:
                    datos = updateData()
                    datos_actualizados = modulo.jugarJug(datos)
                    saveData(datos_actualizados)
                case 3:
                    print(modulo.reglas)
                    input('Enter para volver al menú.....')
                case 4:
                    print("Saliendo del juego...")
                    isActive = False
                case _:
                    print("Opción no válida. Por favor, elija una opción correcta.")
        except ValueError:
            input('Elija una opción correcta. Presione Enter para continuar...')

    print("¡Gracias por jugar!")