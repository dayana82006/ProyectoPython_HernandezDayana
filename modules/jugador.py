import modules as mdls
from modules.jsonM import saveData, updateData

def jugarJug(ptos: dict):
    nombreC = input('🃟 Ingrese nombre completo: ')
    user = input('🃟 Registre su nombre de usuario1: ')
    nombreC2 = input('🃟 Ingrese nombre completo del jugador 2: ')
    user2 = input('🃟 Registre su nombre de usuario2: ')

    userIdx = next((i for i, data in ptos.items() if data['users'] == user), None)
    
    if userIdx is None:
        contadorJvJ = {
            'users': {
                'nombreC': nombreC,
                'nombreC2': nombreC2,
                'nickname': user,
                'nickname2': user2,
            },
            'puntos': {
                'puntosJ1': 0,
                'puntosJ2': 0,
                'rondasJ1': 0,
                'rondasJ2': 0,
                'resultados': 0,
                'rondasGCJ1': 0,
                'rondasGCJ2': 0,
                'escudoJ1': False,
                'escudoJ2': False
            }
        }
        ptos[str(len(ptos) + 1)] = contadorJvJ
    else:
        contadorJvJ = ptos[userIdx]

    print(f'Los usuarios {user} y {user2} se han registrado correctamente')
    
    if contadorJvJ['users']['nickname'] == contadorJvJ['users']['nickname2']:
        print('Este usuario no está disponible')
        input('Presione enter para volver al menú')
        return ptos

    while contadorJvJ['puntos']['rondasJ1'] < 3 and contadorJvJ['puntos']['rondasJ2'] < 3:
        print(mdls.opcPC)
        opcJ1 = input('Jugador 1 elige: ').lower()
        opcJ2 = input('Jugador 2 elige: ').lower()

        if opcJ1 not in ['piedra', 'papel', 'tijera'] or opcJ2 not in ['piedra', 'papel', 'tijera']:
            print('Digite un dato correcto')
            input('Presione cualquier tecla para volver a intentar...')
            continue

        if (opcJ1 == 'piedra' and opcJ2 == 'tijera') or (opcJ1 == 'papel' and opcJ2 == 'piedra') or (opcJ1 == 'tijera' and opcJ2 == 'papel'):
            contadorJvJ['puntos']['rondasGCJ1'] += 1
            contadorJvJ['puntos']['rondasGCJ2'] = 0
            if contadorJvJ['puntos']['rondasGCJ1'] == 2 and not contadorJvJ['puntos']['escudoJ1']:
                contadorJvJ['puntos']['escudoJ1'] = True
                print(f'{user} ha obtenido un escudo por dos victorias consecutivas!')
            print(f'Va ganando {user}')
            contadorJvJ['puntos']['rondasJ1'] += 1
        elif (opcJ2 == 'piedra' and opcJ1 == 'tijera') or (opcJ2 == 'papel' and opcJ1 == 'piedra') or (opcJ2 == 'tijera' and opcJ1 == 'papel'):
            contadorJvJ['puntos']['rondasGCJ2'] += 1
            contadorJvJ['puntos']['rondasGCJ1'] = 0
            if contadorJvJ['puntos']['rondasGCJ2'] == 2 and not contadorJvJ['puntos']['escudoJ2']:
                contadorJvJ['puntos']['escudoJ2'] = True
                print(f'{user2} ha obtenido un escudo por dos victorias consecutivas!')
            if contadorJvJ['puntos']['escudoJ1']:
                print(f'{user} ha usado su escudo y se salva de la derrota!')
                contadorJvJ['puntos']['escudoJ1'] = False
            else:
                print(f'{user2} Ha ganado esta ronda')
                contadorJvJ['puntos']['rondasJ2'] += 1
        else:
            print('Esto es un empate, se han acabado las rachas')
            contadorJvJ['puntos']['rondasGCJ1'] = 0
            contadorJvJ['puntos']['rondasGCJ2'] = 0

        print(f'MARCADOR {contadorJvJ["puntos"]["rondasJ1"]} - {contadorJvJ["puntos"]["rondasJ2"]}')
        print(f'Victorias consecutivas de {user}: {contadorJvJ["puntos"]["rondasGCJ1"]}')
        print(f'Victorias consecutivas de {user2}: {contadorJvJ["puntos"]["rondasGCJ2"]}')
        print(f'Escudo de {user}: {"Activo" if contadorJvJ["puntos"]["escudoJ1"] else "Inactivo"}')
        print(f'Escudo de {user2}: {"Activo" if contadorJvJ["puntos"]["escudoJ2"] else "Inactivo"}')

    print('La partida ha finalizado')
    if contadorJvJ['puntos']['rondasJ1'] > contadorJvJ['puntos']['rondasJ2']:
        print(f'✵°✵.｡.✰ FELICIDADES {contadorJvJ["users"]["nickname"]} GANASTE !! ✰.｡.✵°✵')
        print(f'LO SIENTO {contadorJvJ["users"]["nickname2"]} HAS PERDIDO ٩꒰´·⌢•｀꒱۶⁼³₌₃')
    else:
        print(f'✵°✵.｡.✰ FELICIDADES {contadorJvJ["users"]["nickname2"]} GANASTE !! ✰.｡.✵°✵')
        print(f'LO SIENTO {contadorJvJ["users"]["nickname"]} HAS PERDIDO ٩꒰´·⌢•｀꒱۶⁼³₌₃')

    mdls.pausar_pantalla()

    contadorJvJ['puntos']['rondasJ1'] = 0
    contadorJvJ['puntos']['rondasJ2'] = 0

    saveData(ptos)
    return ptos