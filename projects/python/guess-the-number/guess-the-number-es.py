# Importar la función randint del módulo random
from random import randint

# Definir una función para imprimir el mensaje de bienvenida
def mensaje_bienvenida():
    print("¡Bienvenido al juego Adivina el Número!\n")

# Definir una función para generar un número aleatorio entre 1 y 100
def generar_numero_aleatorio():
    print("Estoy pensando en un número entre 1 y 100. ¡Intenta adivinarlo!")
    return randint(1, 100)

# Definir una función para imprimir un mensaje de felicitaciones basado en el número de intentos
def mensaje_felicitaciones(numero_de_intentos):
    if numero_de_intentos == 1:
        print("\n¡Felicitaciones, adivinaste el número en solo un intento!")
    else:
        print("\n¡Felicitaciones, adivinaste el número en {} intentos!".format(numero_de_intentos))

# Definir una función para obtener el intento del usuario y manejar la validación de la entrada
def obtener_intentodelusuario():
    while True:
        try:
            intento_usuario = int(input("\nIngresa un número entre 1 y 100: "))
            if 1 <= intento_usuario <= 100:
                return intento_usuario
            else:
                print("ERROR: Debes ingresar un número entre 1 y 100.")
        except ValueError:
            print("ERROR: Debes ingresar un número válido.")

# Definir la función principal del juego
def iniciar_juego():
    mensaje_bienvenida()  # Imprimir el mensaje de bienvenida
    numero_aleatorio = generar_numero_aleatorio()  # Generar un número aleatorio
    numero_de_intentos = 0  # Inicializar el contador de intentos
    while True:
        numero_de_intentos += 1  # Incrementar el contador de intentos
        intento_usuario = obtener_intentodelusuario()  # Obtener el intento del usuario
        if intento_usuario == numero_aleatorio:  # Verificar si el intento es correcto
            mensaje_felicitaciones(numero_de_intentos)  # Imprimir el mensaje de felicitaciones
            break  # Salir del ciclo del juego
        elif intento_usuario < numero_aleatorio:
            print("\nEl número que estás buscando es mayor.")
        else:
            print("\nEl número que estás buscando es menor.")
    print("\n¡Gracias por jugar Adivina el Número!")

# Iniciar la partida
if __name__ == "__main__":
    iniciar_juego()  # Iniciar el juego

# Marc Delgado Ferreres