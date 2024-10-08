import os
import sys
import random

import modules as mdls
from modules.jsonM import saveData, updateData

def jugarPc(ptos: dict):
    isActive = True
    user = input('🃟 Registre su nombre de usuario: ')
    userIdx = next((i for i, data in ptos.items() if data['users'] == user), None)
    if userIdx is None:
        
        contador = {
            'users': user,
            'puntos': {
                'PuntosPc': 0,
                'PuntosUs': 0,
                'rondasGU': 0,
                'rondasGM': 0,
                'resultados': 0,
                'escudoUs': False,
                'escudoPc': False,
                'victoriasConsecutivas': 0
            }
        }
        ptos[str(len(ptos) + 1)] = contador
    else:
        
        contador = ptos[userIdx]
    
    print(f'El usuario {user} se ha registrado satisfactoriamente')
    print('USTED JUGARA CONTRA EL PC')
    
    while isActive:
       while isActive:
        maquina=['piedra', 'papel', 'tijera']
        if (contador['puntos']['rondasGM'])<3 and (contador['puntos']['rondasGU'])<3:
            print(mdls.opcPC)
            opcUs=(input('ELije sabiamente: ')).lower()
            opcionPc=random.choice(maquina)
            if opcUs=='piedra' and opcionPc=='tijera':
                print('Eso es, Has ganado')
                (contador['puntos']['rondasGM'])+=1
                print(f"MARCADOR {contador['puntos']['rondasGM']} - {contador['puntos']['rondasGU']}")

            elif opcUs=='papel' and opcionPc=='piedra':
                print('Bien Has ganado')
                (contador['puntos']['rondasGU'])+=1
                print(f"MARCADOR {contador['puntos']['rondasGM']} - {contador['puntos']['rondasGU']}")
            elif opcUs=='tijera' and opcionPc=='papel':
                print('Ey!, Muy bien Has ganado')
                (contador['puntos']['rondasGU'])+=1
                print(f"MARCADOR {contador['puntos']['rondasGM']} - {contador['puntos']['rondasGU']}")
            elif opcionPc=='piedra' and opcUs=='tijera':
                print('Lo siento, no ganaste esta partida')
                (contador['puntos']['rondasGM'])+=1
                print(f"MARCADOR {contador['puntos']['rondasGM']} - {contador['puntos']['rondasGU']}")
            elif opcionPc=='papel' and opcUs=='piedra':
                print('Que triste, no ganaste esta partida')
                (contador['puntos']['rondasGM'])+=1
                print(f"MARCADOR {contador['puntos']['rondasGM']} - {contador['puntos']['rondasGU']}")
            elif opcionPc=='tijera' and opcUs=='papel':
                print('Bueno, no ganaste esta partida')
                (contador['puntos']['rondasGM'])+=1
                print(f"MARCADOR {contador['puntos']['rondasGM']} - {contador['puntos']['rondasGU']}")
            elif opcUs==opcionPc:
                print('Es un empate... Aun puedes ganar!')   
                print(f"MARCADOR {contador['puntos']['rondasGM']} - {contador['puntos']['rondasGU']}")
            else:
                print('digite un dato correcto')
                input('Presione cualquier tecla para volver a intentar...')
        else:
            print('La partida ha finalizado')
            if contador['puntos']['rondasGU'] > contador['puntos']['rondasGM']:
             print(f'✵°✵.｡.✰ FELICIDADES GANASTE !! ✰.｡.✵°✵')
             mdls.pausar_pantalla()
             isActive=False
             contador['puntos']['rondasGU']=0
             contador['puntos']['rondasGM']=0
             contador['puntos']['PuntosUs']+=2
            else:
             print(f"LO SIENTO {user} HAS PERDIDO ٩꒰´·⌢•｀꒱۶⁼³₌₃")
             mdls.pausar_pantalla()
             isActive=False
             contador['puntos']['rondasGU']=0
             contador['puntos']['rondasGM']=0
             contador['puntos']['PuntosPc']+=2

        saveData(ptos)
    
    return ptos 

