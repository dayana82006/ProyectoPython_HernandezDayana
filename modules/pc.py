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
    print('USTED JUGARA CONTRA EL PC')
    isActive=True
    user=str(input('🃟 Registre su nombre de usuario: '))
    users={
            'name':user
            }
    while isActive:
        maquina=['piedra', 'papel', 'tijera']
        if contador['rondasGU']<3 and contador['rondasGM']<3:
            print(mdls.opcPC)
            opcUs=(input('ELije sabiamente: ')).lower()
            opcionPc=random.choice(maquina)
            if opcUs=='piedra' and opcionPc=='tijera':
                print('Has ganado')
                contador['rondasGU']+=1
                #print(tabulate(contador, headers="keys", tablefmt="grid"))
            elif opcUs=='papel' and opcionPc=='piedra':
                print('Has ganado')
                contador['rondasGU']+=1
            elif opcUs=='tijera' and opcionPc=='papel':
                    print('Has ganado')
                    contador['rondasGU']+=1
            elif opcionPc=='piedra' and opcUs=='tijera':
                print('Has perdido')
                contador['rondasGM']+=1
            elif opcionPc=='papel' and opcUs=='piedra':
                print('Has perdido')
                contador['rondasGM']+=1
            elif opcionPc=='tijera' and opcUs=='papel':
                print('Has perdido')
                contador['rondasGM']+=1
            elif opcUs==opcionPc:
                print('Empate')
            elif opcUs != maquina:
                print('digite un dato correcto')
                input('Presione cualquier tecla para volver a intentar...')
            else:
                print('limite')
                isActive=False
        else:
            print('La partida ha finalizado')
            if contador['rondasGU'] > contador['rondasGM']:
             print(f'`✵•.¸,✵°✵.｡.✰ FELICIDADES {users.get('name')} GANASTE !! ✰.｡.✵°✵,¸.•✵´')
             mdls.pausar_pantalla()
            else:
             print('LO SIENTO HAS PERDIDO ٩꒰´·⌢•｀꒱۶⁼³₌₃')
            isActive=False
       