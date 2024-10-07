import os
import sys
import modules as modulo
marcador={}
modulo.checkFile(marcador)
marcador=modulo.readFile()
if __name__=='__main__':


    isActive=True
    
    while isActive:
        #try:
            print(modulo.menu)
            opcion=int(input('Escriba aqui la opcion: '))
            match opcion:
                case 1:
                   #a modulo.jugarPc(marcador)
                    modulo.addData(marcador)
                case 2:
                    modulo.jugarJug(marcador)
                    modulo.addData(marcador
                                   )
                case 3:
                    print(modulo.reglas)
                    input('Enter para volver al menú.....')
                
        #except:
           # input('Elija una opcion correcta ')