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
                'victoriasConsecutivas': 0,
                'victoriasConsecutivasPc': 0
            }
        }
        ptos[str(len(ptos) + 1)] = contador
    else:
        
        contador = ptos[userIdx]
    
    print(f'El usuario {user} se ha registrado satisfactoriamente')
    print('USTED JUGARA CONTRA EL PC')
    
    while isActive:
        #tenemos las opciones
        opciones=['piedra', 'papel', 'tijera']
        #comprobamos si las rondas ganadas por cada uno son menor a 3
        if (contador['puntos']['rondasGM'])<3 and (contador['puntos']['rondasGU'])<3:
            print(mdls.opcPC)
            #le pedimos al user nos de la opcion que desea
            opcUs=(input('ELije sabiamente: ')).lower()
            #y comprobamos que si escribe un dato random, no deje pasar al siguiente paso
            if opcUs not in opciones:
                print('Digite un dato correcto')
            opcionPc=random.choice(opciones)
            #empezamos validando las posibles opciones donde el user gana
            if (opcUs=='piedra' and opcionPc=='tijera') or (opcUs=='papel' and opcionPc=='piedra') or (opcUs=='tijera' and opcionPc=='papel'):
                (contador['puntos']['rondasGU'])+=1
                (contador['puntos']['victoriasConsecutivas'])=+1
                (contador['puntos']['victoriasConsecutivasPc'])=0
                if (contador['puntos']['victoriasConsecutivas'])==2 and not (contador['puntos']['escudoUs']):
                    (contador['puntos']['escudoUs'])=True
                    print(f'{user} ha ganado un escudo')
                print(f"MARCADOR {contador['puntos']['rondasGM']} - {contador['puntos']['rondasGU']}")
            #validamos las opciones donde la maquina puede ganar    
            elif opcionPc=='papel' and opcUs=='piedra' or opcionPc=='piedra' and opcUs=='tijera' or opcionPc=='tijera' and opcUs=='papel':
                print('No ganaste esta partida')
                (contador['puntos']['rondasGM'])+=1
                (contador['puntos']['victoriasConsecutivasPc'])+=1
                (contador['puntos']['victoriasConsecutivas'])=0
                if (contador['puntos']['victoriasConsecutivasPc'])==2 and not (contador['puntos']['escudoPc']):
                    (contador['puntos']['escudoPc'])=True
                    print('La IA tiene un escudo')
                print(f"MARCADOR {contador['puntos']['rondasGM']} - {contador['puntos']['rondasGU']}")
                if contador['puntos']['escudoUs']:
                    print(f'{user} ha usado su escudo y se salva de la derrota!')
                    contador['puntos']['escudoUs'] = False
                else:
                    print('Pc Ha ganado esta ronda')
                    contador['puntos']['rondasGM'] += 1
            elif opcUs==opcionPc:
                print('Esto es un empate, se han acabado las rachas')
                contador['puntos']['victoriasConsecutivas'] = 0
                contador['puntos']['victoriasConsecutivasPc'] = 0     
            
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

