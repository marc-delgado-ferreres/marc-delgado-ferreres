# Importar la función randint del módulo random
from random import choice

# Importar la función system del módulo os
from os import system

# Limpia la consola para mejorar la presentación visual
def limpiar_consola():
    system("cls")

# Devuelve una opción aleatoria entre "piedra", "papel" y "tijera"
def obtener_opcion_aleatoria():
    opciones = ("piedra", "papel", "tijera")
    return choice(opciones)

# Compara las opciones del jugador y la máquina para determinar el resultado
def comparar_opciones(opcion_jugador, opcion_aleatoria):
    resultados = {
        ("piedra", "tijera"): "jugador",
        ("papel", "piedra"): "jugador",
        ("tijera", "papel"): "jugador"
    }
    return "empate" if opcion_jugador == opcion_aleatoria else resultados.get((opcion_jugador, opcion_aleatoria), "aleatoria")

# Muestra el menú de opciones para que el jugador elija
def mostrar_menu():
    print("Piedra Papel Tijera:\n")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    print("4. Salir\n")

# Obtiene la opción elegida por el jugador y la devuelve.
def obtener_opcion_jugador():
    opciones = ("piedra", "papel", "tijera")
    opcion_menu = input("Elige una opción: ")
    while opcion_menu not in ("1", "2", "3", "4"):
        print("ERROR: Opción inválida.")
        opcion_menu = input("\nElige una opción: ")
    if opcion_menu == "4":
        return None
    return opciones[int(opcion_menu) - 1]

# Muestra el resultado del juego
def mostrar_resultado(resultado):
    if resultado == "empate":
        print("\n¡Empate!")
    elif resultado == "jugador":
        print("\n¡Ganaste!")
    else:
        print("\n¡Perdiste!")

# Muestra un mensaje de bienvenida al inicio del juego
def mensaje_bienvenida():
    print("¡Bienvenido al juego de piedra, papel o tijera!\n")

# Muestra un mensaje de despedida al finalizar el juego
def mensaje_fin_juego():
    print("\n¡Gracias por jugar a piedra, papel o tijera!")

# Función principal que inicia el juego y controla su flujo
def iniciar_juego():
    mensaje_bienvenida()
    while True:
        mostrar_menu()
        opcion_jugador = obtener_opcion_jugador()
        if opcion_jugador is None:
            break
        opcion_aleatoria = obtener_opcion_aleatoria()
        print("\n{} vs {}".format(opcion_jugador.title(), opcion_aleatoria.title()))
        resultado = comparar_opciones(opcion_jugador, opcion_aleatoria)
        mostrar_resultado(resultado)
        input("\nPresiona Enter para continuar...")
        limpiar_consola()
    mensaje_fin_juego()

# Iniciar la partida
if __name__ == "__main__":
    iniciar_juego()

# Marc Delgado Ferreres