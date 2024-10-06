import os
import sys
import modules as modulo

if __name__=='__main__':
    
    isActive=True
    
    while isActive:
        try:
            print(modulo.menu)
            opcion=int(input('Escriba aqui la opcion: '))
            match opcion:
                case 1:
                    modulo.jugarPc()
                    
                
                
                
                
        except:
            input('Elija una opcion correcta ')