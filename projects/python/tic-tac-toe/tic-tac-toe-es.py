# Importar la función system del módulo os
from os import system

# Crear el tablero de juego utilizando una lista de listas
tabla = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

# Mostrar un mensaje de bienvenida al inicio del juego
def mensaje_bienvenida():
    print("¡Bienvenido al juego Tres en Raya!\n")

# Dibujar el tablero de juego con los símbolos actuales
def dibujar_tablero():
    print(''' {} | {} | {}
-----------
 {} | {} | {}
-----------
 {} | {} | {}'''.format(tabla[0][0], tabla[0][1], tabla[0][2], tabla[1][0], tabla[1][1], tabla[1][2], tabla[2][0], tabla[2][1], tabla[2][2]))

# Actualizar el tablero con el símbolo del jugador en la fila y columna especificadas
def actualizar_tablero(fila, columna, simbolo_jugador):
    tabla[fila][columna] = simbolo_jugador

# Obtener el nombre del jugador según su símbolo
def obtener_nombre_jugador(simbolo_jugador):
    return "Uno" if simbolo_jugador == "X" else "Dos"

# Verificar si hay una victoria del jugador actual
def verificar_victoria(simbolo_jugador):
    combinaciones_ganadoras = [
        [(0, 0), (1, 1), (2, 2)],
        [(2, 0), (1, 1), (0, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)]
    ]
    for combinacion in combinaciones_ganadoras:
        if all(tabla[x][y] == simbolo_jugador for x, y in combinacion):
            nombre_jugador = obtener_nombre_jugador(simbolo_jugador)
            print("\n¡El Jugador {} ha ganado! El juego ha terminado.".format(nombre_jugador))
            return True
    return False

# Solicitar la posición en el tablero donde el jugador quiere colocar su símbolo
def solicitar_posicion_tablero(simbolo_jugador):
    try:
        while True:
            fila = int(input("\nEscribe la fila [1-3] donde deseas colocar '{}': ".format(simbolo_jugador))) - 1
            columna = int(input("Escribe la columna [1-3] donde deseas colocar '{}': ".format(simbolo_jugador))) - 1
            if 0 <= fila <= 2 and 0 <= columna <= 2:
                if tabla[fila][columna] == " ":
                    system("cls") # Limpiar la consola (Windows)
                    return fila, columna
                else:
                    print("ERROR: No puedes colocar un símbolo encima de otro símbolo.")
            else:
                print("ERROR: Por favor, escribe solo números entre 1 y 3.")
    except:
        print("ERROR: Por favor, escribe solo números entre 1 y 3.")
        fila, columna = solicitar_posicion_tablero(simbolo_jugador)
        return fila, columna

# Mostrar el mensaje de fin de juego en caso de empate
def mensaje_fin_juego_empate():
    input("\n¡Felicidades jugadores, han empatado! El juego ha terminado.")
    exit()

# Realizar el turno del jugador actual
def turno_jugador(simbolo_jugador):
    nombre_jugador = obtener_nombre_jugador(simbolo_jugador)
    print("\nTurno del Jugador {}.".format(nombre_jugador))
    fila, columna = solicitar_posicion_tablero(simbolo_jugador)
    actualizar_tablero(fila, columna, simbolo_jugador)
    dibujar_tablero()
    if verificar_victoria(simbolo_jugador):
        exit()

# Iniciar el juego
def iniciar_juego():
    mensaje_bienvenida()
    dibujar_tablero()
    for i in range(9):
        simbolo_jugador = "X" if i % 2 == 0 else "O"
        turno_jugador(simbolo_jugador)
    mensaje_fin_juego_empate()

# Iniciar la partida
if __name__ == "__main__":
    iniciar_juego()

# Marc Delgado Ferreres