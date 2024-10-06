import os 
import sys
import modules as mdls
import random
#from tabulate import tabulate

contador={
    'PuntosPc':0,
    'PuntosUs':0,
    'rondasGU':0,
    'rondasGM':0,
    'resultados':0
}
def jugarPc():
    
    isActive=True
    user=str(input('🃟 Registre su nombre de usuario: '))
    users={
            'name':user
            }
    print('USTED JUGARA CONTRA EL PC')
    while isActive:
        maquina=['piedra', 'papel', 'tijera']
        if contador['rondasGU']<3 and contador['rondasGM']<3:
            print(mdls.opcPC)
            opcUs=(input('ELije sabiamente: ')).lower()
            opcionPc=random.choice(maquina)
            if opcUs=='piedra' and opcionPc=='tijera':
                print('Eso es, Has ganado')
                contador['rondasGU']+=1
                print(f'MARCADOR {contador.get('PuntosPC')} - {contador.get('PuntosUs')}')

            elif opcUs=='papel' and opcionPc=='piedra':
                print('Bien Has ganado')
                contador['rondasGU']+=1
                print(f'MARCADOR {contador.get('PuntosPC')} - {contador.get('PuntosUs')}')
            elif opcUs=='tijera' and opcionPc=='papel':
                    print('Ey !, Muy bien Has ganado')
                    contador['rondasGU']+=1
                    print(f'MARCADOR {contador.get('PuntosPC')} - {contador.get('PuntosUs')}')
            elif opcionPc=='piedra' and opcUs=='tijera':
                print('Lo siento, Has perdido')
                contador['rondasGM']+=1
                print(f'MARCADOR {contador.get('PuntosPC')} - {contador.get('PuntosUs')}')
            elif opcionPc=='papel' and opcUs=='piedra':
                print('Que triste, Has perdido')
                contador['rondasGM']+=1
                print(f'MARCADOR {contador.get('PuntosPC')} - {contador.get('PuntosUs')}')
            elif opcionPc=='tijera' and opcUs=='papel':
                print('Bueno, Has perdido')
                contador['rondasGM']+=1
                print(f'MARCADOR {contador.get('PuntosPC')} - {contador.get('PuntosUs')}')
            elif opcUs==opcionPc:
                print('Es un empate... Aun puedes ganar!')   
                print(f'MARCADOR {contador.get('PuntosPC')} - {contador.get('PuntosUs')}') 
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
            
       