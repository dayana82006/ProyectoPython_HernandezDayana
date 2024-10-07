import os 
import sys
import modules as mdls
import random
def jugarPc(ptos:dict):
    isActive=True
    user=str(input('🃟 Registre su nombre de usuario: '))
    contador={
        'users':user,
        'puntos':{ 
            'PuntosPc':0,
            'PuntosUs':0,
            'rondasGU':0,
            'rondasGM':0,
            'resultados':0
         }
    }
    ptos.update({int(len(ptos))+1:contador}) 
    print(f'El usuario {(contador['users']['user'])} se ha registrado satisfactoriamente') 
    print('USTED JUGARA CONTRA EL PC')
    while isActive:
        maquina=['piedra', 'papel', 'tijera']
        if (contador['puntos']['rondasGM'])<3 and (contador['puntos']['rondasGU'])<3:
            print(mdls.opcPC)
            opcUs=(input('ELije sabiamente: ')).lower()
            opcionPc=random.choice(maquina)
            if opcUs=='piedra' and opcionPc=='tijera':
                print('Eso es, Has ganado')
                (contador['puntos']['rondasGM'])+=1
                print(f'MARCADOR {(contador.get('PuntosPC'))} - {(contador['puntos']['PuntosUs'])}')

            elif opcUs=='papel' and opcionPc=='piedra':
                print('Bien Has ganado')
                (contador['puntos']['rondasGU'])+=1
                print(f'MARCADOR {(contador.get('PuntosPC'))} - {(contador['puntos']['PuntosUs'])}')
            elif opcUs=='tijera' and opcionPc=='papel':
                print('Ey!, Muy bien Has ganado')
                (contador['puntos']['rondasGU'])+=1
                print(f'MARCADOR {(contador.get('PuntosPC'))} - {(contador['puntos']['PuntosUs'])}')
            elif opcionPc=='piedra' and opcUs=='tijera':
                print('Lo siento, no ganaste esta partida')
                (contador['puntos']['rondasGM'])+=1
                print(f'MARCADOR {(contador.get('PuntosPC'))} - {(contador['puntos']['PuntosUs'])}')
            elif opcionPc=='papel' and opcUs=='piedra':
                print('Que triste, no ganaste esta partida')
                (contador['puntos']['rondasGM'])+=1
                print(f'MARCADOR {(contador.get('PuntosPC'))} - {(contador['puntos']['PuntosUs'])}')
            elif opcionPc=='tijera' and opcUs=='papel':
                print('Bueno, no ganaste esta partida')
                (contador['puntos']['rondasGM'])+=1
                print(f'MARCADOR {(contador.get('PuntosPC'))} - {(contador['puntos']['PuntosUs'])}')
            elif opcUs==opcionPc:
                print('Es un empate... Aun puedes ganar!')   
                print(f'MARCADOR{(contador.get('PuntosPC'))} - {(contador['puntos']['PuntosUs'])}') 
            else:
                print('digite un dato correcto')
                input('Presione cualquier tecla para volver a intentar...')
        else:
            print('La partida ha finalizado')
            if (contador['puntos']['rondasGU']) > (contador['puntos']['rondasGM']):
             print(f'✵°✵.｡.✰ FELICIDADES {(contador['users']['user'])} GANASTE !! ✰.｡.✵°✵')
             mdls.pausar_pantalla()
             isActive=False
             (contador['puntos']['rondasGU'])=0
             (contador['puntos']['rondasGM'])=0
            else:
             print(f'LO SIENTO {(contador['users']['user'])} HAS PERDIDO ٩꒰´·⌢•｀꒱۶⁼³₌₃')
             isActive=False
             (contador['puntos']['rondasGU'])=0
             (contador['puntos']['rondasGM'])=0
            
       