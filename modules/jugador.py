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

    isActive=True
    user=str(input('🃟 Registre su nombre de usuario1: '))
    user2=str(input('🃟 Registre su nombre de usuario2: '))
    users={
            'name':user,
            'name2':user2
            }
    
    
    while isActive:
        opciones=['piedra', 'papel', 'tijera']
        if contador['rondasJ1']<3 and contador['rondasJ2']<3:
            print(mdls.opcPC)
            opcJ1=(input('Jugador 1 elije: ')).lower()
            opcJ2=(input('Jugador 2 elije: ')).lower()
            if opcJ1=='piedra' and opcJ2=='tijera':
                print(f'Va ganando {user}')
                contador['rondasJ1']+=1
                print(f'MARCADOR {contador["rondasJ2"]} - {contador["rondasJ1"]}')
            elif opcJ1=='papel' and opcJ2=='piedra':
                print(f'{user} Ha ganado esta ronda')
                contador['rondasJ1']+=1
                print(f'MARCADOR {contador["rondasJ2"]} - {contador["rondasJ1"]}')
            elif opcJ1=='tijera' and opcJ2=='':
                print(f'{user} Ha ganado esta ronda')
                contador['rondasJ1']+=1
                print(f'MARCADOR {contador["rondasJ2"]} - {contador["rondasJ1"]}')
            elif opcJ2=='piedra' and opcJ1=='tijera':
                print(f'{user2} Ha ganade esta ronda') 
                contador['rondasJ2']+=1
                print(f'MARCADOR {contador.get("rondasJ2")} - {contador["rondasJ1"]}')
            elif opcJ2=='papel' and opcJ1=='piedra':
                print(f'{user2} Ha ganado esta ronda') 
                contador['rondasJ2']+=1
                print(f'MARCADOR {contador.get("rondasJ2")} - {contador["rondasJ1"]}')
            elif opcJ2=='tijera' and opcJ1=='papel':
               print(f'{user2} Ha ganado esta ronda') 
               contador['rondasJ2']+=1
               print(f'MARCADOR {contador.get("rondasJ2")} - {contador["rondasJ1"]}')
            elif opcJ1==opcJ2:
                print('Esto es un empate, re reinicia marcador') 
                contador["rondasJ2"]=0
                contador["rondasJ1"]=0

                print(f'MARCADOR {contador.get("rondasJ2")} - {contador["rondasJ1"]}')
            else:
                print('digite un dato correcto')
                input('Presione cualquier tecla para volver a intentar...')
        else:
            print('La partida ha finalizado')
            if contador['rondasJ1'] > contador['rondasJ2']:
             print(f'✵°✵.｡.✰ FELICIDADES {users["name"]} GANASTE !! ✰.｡.✵°✵')
             print(f'LO SIENTO {users["name2"]} HAS PERDIDO ٩꒰´·⌢•｀꒱۶⁼³₌₃')
             mdls.pausar_pantalla()
             isActive=False
             contador['rondasJ1']=0
             contador['rondasJ2']=0
            else:
             print(f'✵°✵.｡.✰ FELICIDADES {users["name2"]} GANASTE !! ✰.｡.✵°✵')
             print(f'LO SIENTO {users["name"]} HAS PERDIDO ٩꒰´·⌢•｀꒱۶⁼³₌₃')
             mdls.pausar_pantalla()
             return(jugarJug)
             isActive=False
             contador['rondasJ1']=0
             contador['rondasJ2']=0
            
       