import modules as mdls
import os
import sys

def jugarJug():
    contador={
        'PuntosJ1':0,
        'PuntosJ2':0,
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
                contador['PuntosJ1']+=2
                print(f'MARCADOR {contador.get('PuntosJ2')} - {contador.get('PuntosJ1')}')
            elif opcJ1=='papel' and opcJ2=='piedra':
                print(f'{user} Ha ganado esta ronda')
                contador['PuntosJ1']+=2
                contador['rondasJ1']+=1
                print(f'MARCADOR {contador.get('PuntosJ2')} - {contador.get('PuntosJ1')}')
            elif opcJ1=='tijera' and opcJ2=='papel':
                print(f'Va ganando {user}')
                contador['rondasJ1']+=1
                contador['PuntosJ1']+=2
                print(f'MARCADOR {contador.get('PuntosJ2')} - {contador.get('PuntosJ1')}')
            elif opcJ2=='piedra' and opcJ1=='tijera':
                print(f'{user2} Ha ganadoe sta ronda')
                contador['PuntosJ2']+=2
                contador['rondasJ2']+=1
                print(f'MARCADOR {contador.get('PuntosJ2')} - {contador.get('PuntosJ2')}')
            elif opcJ2=='papel' and opcJ1=='piedra':
                
            elif opcJ2=='tijera' and opcJ1=='papel':
               
            elif opcJ1==opcJ2:
                 
            else:
                print('digite un dato correcto')
                input('Presione cualquier tecla para volver a intentar...')
        else:
            print('La partida ha finalizado')
            if contador['rondasGU'] > contador['rondasGM']:
             print(f'✵°✵.｡.✰ FELICIDADES {users.get('name')} GANASTE !! ✰.｡.✵°✵')
             mdls.pausar_pantalla()
             isActive=False
             contador['rondasGU']=0
             contador['rondasGM']=0
            else:
             print(f'LO SIENTO {users.get('name')} HAS PERDIDO ٩꒰´·⌢•｀꒱۶⁼³₌₃')
             isActive=False
             contador['rondasGU']=0
             contador['rondasGM']=0
            
       