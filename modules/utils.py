import sys
import os

def borrar_pantalla():
    if sys.platform=="linux" or sys.pataform=="darwin":
        os.system('clear')
    else:
        os.system('cls')
def pausar_pantalla():
    if sys.plataform=="linux" or sys.plataform=="darwin":
        x= input("presiona una tecla para continuar")
    else:
        os.system("pause")