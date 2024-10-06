def validateData(message:str):
    global isAllow 
    flagFunction = True
    opciones = ('N','n','S','s')
    try:
        accion = input(f'{message}').upper()
        if (accion not in opciones):
            print('La opcion que ud ingreso no esta permitida.......')
            validateData()
        elif (accion== 'N' ):
            flagFunction = True
        elif  ((accion) == 'S'):
            flagFunction = False
        return flagFunction
    except TypeError:
        validateData(message)

def validateResponse(message:str):
    global isAllow
    flagFunction = True
    opciones = ('N','n','S','s')
    try:
        accion = input(f'{message}').upper()
        if (accion not in opciones):
            print('La opcion que ud ingreso no esta permitida.......')
            validateData()
        elif (accion== 'S' ):
            flagFunction = True
        elif  ((accion) == 'N'):
            flagFunction = False
        return flagFunction
    except TypeError:
        validateResponse(message)