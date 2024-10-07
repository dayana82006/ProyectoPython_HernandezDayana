import modules as mdls
import os
import sys

def jugarJug(marcador):
    contador={
        'puntosJ1':0,
        'puntosJ2':0,
        'rondasJ1':0,
        'rondasJ2':0,
        'resultados':0
    }
    rondasGCJ1 = 0  
    rondasGCJ2 = 0  
    escudoJ1 = False
    escudoJ2 = False
    nombreC=str(input('🃟 Ingrese su nombre completo'))
    user=str(input('🃟 Registre su nombre de usuario1: '))
    user2=str(input('🃟 Registre su nombre de usuario2: '))
    users={  
            'nickname':user,
            'nickname2':user2
            }
    
    if users.get("nickname") == users.get("nickname2"):
            print('Este usuario no esta disponible')
            isActive=False
            input('Presiones enter para volver al menu')
    else:
        isActive=True
    while isActive:
        opciones=['piedra', 'papel', 'tijera']
        if contador['rondasJ1']<3 and contador['rondasJ2']<3:
            print(mdls.opcPC)
            opcJ1=(input('Jugador 1 elije: ')).lower()
            opcJ2=(input('Jugador 2 elije: ')).lower()
            if opcJ1=='piedra' and opcJ2=='tijera' or opcJ1=='papel' and opcJ2=='piedra' or opcJ1=='tijera' and opcJ2=='papel':
                rondasGCJ1 += 1
                rondasGCJ2 = 0
                if rondasGCJ1 == 2 and not escudoJ1:
                    escudoJ1 = True 
                    print(f'{user} ha obtenido un escudo por dos victorias consecutivas!')
                print(f'Va ganando {user}')
                contador['rondasJ1']+=1
                print(f'MARCADOR {contador["rondasJ2"]} - {contador["rondasJ1"]}')
            elif opcJ2=='piedra' and opcJ1=='tijera' or opcJ2=='papel' and opcJ1=='piedra' or opcJ2=='tijera' and opcJ1=='papel':
                rondasGCJ2 += 1
                rondasGCJ1 = 0
                if rondasGCJ2 == 2 and not escudoJ2:
                    escudoJ2 = True
                    print(f'{user2} ha obtenido un escudo por dos victorias consecutivas!')
                if escudoJ1:
                    print(f'{user} ha usado su escudo y se salva de la derrota!')
                    escudoJ1 = False
                else:
                    print(f'{user2} Ha ganado esta ronda') 
                    contador['rondasJ2']+=1
                print(f'MARCADOR {contador.get("rondasJ2")} - {contador["rondasJ1"]}')
            elif opcJ1==opcJ2:
                print('Esto es un empate, se han acabado las rachas') 
                rondasGCJ1 = 0
                rondasGCJ2 = 0
                print(f'MARCADOR {contador.get("rondasJ2")} - {contador["rondasJ1"]}')
            else:
                print('digite un dato correcto')
                input('Presione cualquier tecla para volver a intentar...')
            
            print(f'Victorias consecutivas de {user}: {rondasGCJ1}')
            print(f'Victorias consecutivas de {user2}: {rondasGCJ2}')
            print(f'Escudo de {user}: {"Activo" if escudoJ1 else "Inactivo"}')
            print(f'Escudo de {user2}: {"Activo" if escudoJ2 else "Inactivo"}')
        else:
            print('La partida ha finalizado')
            if contador['rondasJ1'] > contador['rondasJ2']:
             print(f'✵°✵.｡.✰ FELICIDADES {users["nickname"]} GANASTE !! ✰.｡.✵°✵')
             print(f'LO SIENTO {users["nickname2"]} HAS PERDIDO ٩꒰´·⌢•｀꒱۶⁼³₌₃')
             mdls.pausar_pantalla()
             isActive=False
             contador['rondasJ1']=0
             contador['rondasJ2']=0
            else:
             print(f'✵°✵.｡.✰ FELICIDADES {users["nickname2"]} GANASTE !! ✰.｡.✵°✵')
             print(f'LO SIENTO {users["nickname"]} HAS PERDIDO ٩꒰´·⌢•｀꒱۶⁼³₌₃')
             mdls.pausar_pantalla()
             isActive=False
             contador['rondasJ1']=0
             contador['rondasJ2']=0