from random import randint
from time import sleep
from os import system

mazo_palo = ["Picas", "Rombos", "Tréboles", "Corazones"]
mazo_valores = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
valores_cartas = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, [1, 11]]
cartas_usadas = []
nombre_jugadores = ["Crupier"]
cartas_jugadores = [[]]

def mensaje_bienvenida():
    print("¡Bienvenido al juego Blackjack!\n")

def nombre_carta(mazo_palo_aleatorio, mazo_valor_aleatorio):
    return "{} de {}".format(mazo_valores[mazo_valor_aleatorio],  mazo_palo[mazo_palo_aleatorio])

def comprobar_carta(mazo_palo_aleatorio,  mazo_valor_aleatorio):
    if [mazo_palo_aleatorio, mazo_valor_aleatorio] in cartas_usadas:
        return False
    return True

def conseguir_carta_aleatoria():
    mazo_palo_aleatorio = randint(0, 3)
    mazo_valor_aleatorio = randint(0, 12)
    carta_valida = comprobar_carta(mazo_palo_aleatorio, mazo_valor_aleatorio)
    if carta_valida:
        cartas_usadas.append([mazo_palo_aleatorio, mazo_valor_aleatorio])
        return [mazo_palo_aleatorio, mazo_valor_aleatorio]
    else:
        return conseguir_carta_aleatoria()

def conseguir_numero_jugadores():
    try:
        numero_jugadores = 0
        while numero_jugadores > 7 or numero_jugadores < 1:
            numero_jugadores = int(input("Cuántas jugadoras van a jugar: "))
            if numero_jugadores < 1:
                print("ERROR: Para comenzar el juego debe haber al menos un jugador.\n")
            elif numero_jugadores > 7:
                print("ERROR: Como máximo pueden haber siete jugadoras.\n")
            else:
                system("cls")
                return numero_jugadores
    except:
        print("ERROR: Debe de introducir un número entero.\n")
        return conseguir_numero_jugadores()

def actualizar_lista_cartas_jugadores(numero_jugadores):
    for _ in range(numero_jugadores):
        cartas_jugadores.append([])

def nombres_jugadores(numero_jugadores):
    for i in range(numero_jugadores):
        nombre_jugador = input("{}. Cual es el nombre del jugador: ".format(i + 1))
        nombre_jugadores.append(nombre_jugador.title())

def repartir_carta(cartas_jugador):
    carta_aleatoria = conseguir_carta_aleatoria()
    cartas_jugadores[cartas_jugador].append(carta_aleatoria)

def repartir_cartas_inicio(numero_jugadores):
    for _ in range(2):
        for i in range(numero_jugadores):
            repartir_carta(i + 1)
            mostrar_cartas_generales(numero_jugadores)
        repartir_carta(0)
        mostrar_cartas_generales(numero_jugadores)

def mostrar_cartas_generales(numero_jugadores):
    system("cls")
    print("CARTAS")
    for i in range(numero_jugadores + 1):
        jugador_nombre = nombre_jugadores[i]
        jugador_cartas = cartas_jugadores[i]
        print("\n{}:".format(jugador_nombre))
        if jugador_cartas:
            for carta in jugador_cartas:
                print("{}".format(nombre_carta(carta[0], carta[1])))
                if len(jugador_cartas) == 1:
                    print("Sin cartas")
        else:
            print("Sin cartas")
            print("Sin cartas")
    sleep(2)

def mostrar_cartas_individuales(numero_jugador):
    system("cls")
    print("CARTAS")
    jugador_nombre = nombre_jugadores[0]
    jugador_cartas = cartas_jugadores[0]
    print("\n{}:".format(jugador_nombre))
    for carta in jugador_cartas:
        print("{}".format(nombre_carta(carta[0], carta[1])))
    jugador_nombre = nombre_jugadores[numero_jugador]
    jugador_cartas = cartas_jugadores[numero_jugador]
    print("\n{}:".format(jugador_nombre))
    for carta in jugador_cartas:
        print("{}".format(nombre_carta(carta[0], carta[1])))
    opciones(numero_jugador)
    
def opciones(numero_jugador):
    doblar = False
    dividir = False
    if len(jugador_cartas) == 2:
        doblar = True
        jugador_cartas = cartas_jugadores[numero_jugador]
        primera_carta = jugador_cartas[0][-1]
        segunda_carta = jugador_cartas[1][-1]
        posicion_primera_carta = mazo_valores.index(primera_carta)
        posicion_segunda_carta = mazo_valores.index(segunda_carta)
        valor_primera_carta = valores_cartas[posicion_primera_carta]
        valor_segunda_carta = valores_cartas[posicion_segunda_carta]
        if valor_primera_carta == valor_segunda_carta:
            dividir = True
    print("1. Plantarse")
    print("2. Pedir carta")
    if doblar == True:
        print("3. Doblar")
    if dividir == True:
        print("4. Dividir")
    pedir_opcion()

def pedir_opcion():
    opcion = 0
    while opcion < 1 or opcion > 4:
        try:
            opcion = int(input("Que opción elijes: "))
            if 1 <= opcion <= 4:
                realizar_opcion(opcion)
            else:
                print("ERROR: Debes elegir entre [1-4] ")
        except:
            print("ERROR: Debe ser un número entero")
            pedir_opcion()

def realizar_opcion(opcion):
    if opcion == 1:
        # pasamos al siguiente jugador
    elif opcion == 2:
        # Se añade otra carta para el jugador
    elif opcion == 3:
        # El usuario elije doblar por tanto se le da una carta y se pasa al siguiente usuario
    else:
        # Se divide las cartas en 2 haciendo que el jugador tenga 2 manios con las que jugar


def juegooooo():
    game_finished = False
    mensaje_bienvenida()
    numero_jugadores = conseguir_numero_jugadores()
    nombres_jugadores(numero_jugadores)
    actualizar_lista_cartas_jugadores(numero_jugadores)
    while not game_finished:
        repartir_cartas_inicio(numero_jugadores)
        for i in range(numero_jugadores):
            mostrar_cartas_individuales(i + 1)
        game_finished = True

juegooooo()