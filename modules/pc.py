import os
import sys
import random
import modules as mdls
from modules.jsonM import saveData, updateData

def jugarPc(ptos: dict):
    isActive = True
    user = input('🃟 Registre su nombre de usuario: ')
    #el next te da el primer indice que encontro, y si no hay nada devuelve none
    userIdx = next((i for i, data in ptos.items() if data['users'] == user), None)
    if userIdx is None:#si el usuario no esta registrado crea el diciconario 
        #el diccionario que contiene toda la informacion
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
         # Si el usuario ya existe, se obtiene su información
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
                mdls.borrar_pantalla()#me borra la pantalla
                print('Digite un dato correcto')
                
            opcionPc=random.choice(opciones)
            #empezamos validando las posibles opciones donde el user gana
            if (opcUs=='piedra' and opcionPc=='tijera') or (opcUs=='papel' and opcionPc=='piedra') or (opcUs=='tijera' and opcionPc=='papel'):
                #me suma uno al contador
                (contador['puntos']['rondasGU'])+=1
                (contador['puntos']['victoriasConsecutivas'])=+1
                #a las victorias consecutivas de pc no se le suma nada
                (contador['puntos']['victoriasConsecutivasPc'])=0
                #si se suman dos victorias consecutivas y el escudo no esta activo, se activa
                if (contador['puntos']['victoriasConsecutivas'])==2 and not (contador['puntos']['escudoUs']):
                    (contador['puntos']['escudoUs'])=True#activa 
                    print(f'{user} ha ganado un escudo')
                print(f"MARCADOR {contador['puntos']['rondasGM']} - {contador['puntos']['rondasGU']}")
            #validamos las opciones donde la maquina puede ganar    
            elif opcionPc=='papel' and opcUs=='piedra' or opcionPc=='piedra' and opcUs=='tijera' or opcionPc=='tijera' and opcUs=='papel':
                print('No ganaste esta partida')
                (contador['puntos']['rondasGM'])+=1 #mas 1 a las rondas, cuandop se completen 3 se acaba la partida
                (contador['puntos']['victoriasConsecutivasPc'])+=1 # se le suma 1 a la victoria consecutiva y esto va acumulandose para el escudo
                (contador['puntos']['victoriasConsecutivas'])=0
                if (contador['puntos']['victoriasConsecutivasPc'])==2 and not (contador['puntos']['escudoPc']):
                    (contador['puntos']['escudoPc'])=True
                    print('La IA tiene un escudo')
                print(f"MARCADOR {contador['puntos']['rondasGM']} - {contador['puntos']['rondasGU']}")
                   
                # Verifica si el usuario tiene escudo y evita la derrota
                if contador['puntos']['escudoUs']:
                    print(f'{user} ha usado su escudo y se salva de la derrota!')
                    contador['puntos']['escudoUs'] = False#si usa su poder se le quita el escudo
                else:
                    print('Pc Ha ganado esta ronda')
                    contador['puntos']['rondasGM'] += 1
            elif opcUs==opcionPc:
                print('Esto es un empate, se han acabado las rachas')
                contador['puntos']['victoriasConsecutivas'] = 0
                contador['puntos']['victoriasConsecutivasPc'] = 0     
            
        else:
            # Si uno de los jugadores ha ganado 3 rondas, termina el juego
            print('La partida ha finalizado')
            if contador['puntos']['rondasGU'] > contador['puntos']['rondasGM']:
             mdls.borrar_pantalla()
             print(f'✵°✵.｡.✰ FELICIDADES GANASTE !! ✰.｡.✵°✵')
             mdls.pausar_pantalla()
             isActive=False
             #se reinicia el contador y se le suma los dos a la partida
             contador['puntos']['rondasGU']=0
             contador['puntos']['rondasGM']=0
             contador['puntos']['PuntosUs']+=2
            else:
             print(f"LO SIENTO {user} HAS PERDIDO ٩꒰´·⌢•｀꒱۶⁼³₌₃")
             mdls.borrar_pantalla()
             mdls.pausar_pantalla()
             isActive=False
             #se reinicia el contador para volver a jugar partida y se le suma los dos puntos
             contador['puntos']['rondasGU']=0
             contador['puntos']['rondasGM']=0
             contador['puntos']['PuntosPc']+=2
        #se guarda los datos en el dicionarios ptos
        saveData(ptos)
    
    return ptos  # Devuelve el diccionario actualizado

