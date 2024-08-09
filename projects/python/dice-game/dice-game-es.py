# Importa la función randint desde el módulo random
from random import randint

# Importa la función system desde el módulo os
from os import system

# Muestra un mensaje de bienvenida al iniciar el juego
def mensaje_bienvenida():
    print("¡Bienvenido al Juego de Dados!")

# Permite al usuario elegir los dados con los que jugar.
def solicitar_dado_usuario():
    tipos_de_dados = {1: "D6", 2: "D4", 3: "D8", 4: "D10", 5: "D12", 6: "D120"}
    dados_usuario = []
    while True:
        try:
            dado_usuario = int(input('''\nOpciones de Dados:
1. [D6] Dado de seis caras
2. [D4] Dado de cuatro caras
3. [D8] Dado de ocho caras
4. [D10] Dado de diez caras
5. [D12] Dado de doce caras
6. [D120] Dado de ciento veinte caras
7. Continuar...

Elige el dado que deseas agregar: '''))
            if 1 <= dado_usuario <= 7:
                if dado_usuario == 7:
                    if not dados_usuario:
                        system("cls")
                        print("ERROR: Debes seleccionar al menos un dado.")
                        if len(dados_usuario) > 0:
                            mostrar_dados_usuario(dados_usuario, tipos_de_dados)
                        continue
                    else:
                        break
                dados_usuario.append(dado_usuario)
                dados_usuario.sort() # Ordena los dados de mayor a menor
                mostrar_dados_usuario(dados_usuario, tipos_de_dados)
            else:
                system("cls")
                print("ERROR: Debes ingresar una opción válida.")
                if len(dados_usuario) > 0:
                    mostrar_dados_usuario(dados_usuario, tipos_de_dados)
        except ValueError:
            system("cls")
            print("ERROR: Debes ingresar un número entero.")
            if len(dados_usuario) > 0:
                mostrar_dados_usuario(dados_usuario, tipos_de_dados)

    lanzar_dados(dados_usuario, tipos_de_dados)

# Muestra la lista de dados seleccionados por el usuario
def mostrar_dados_usuario(dados_usuario, tipos_de_dados):
    system("cls")
    print("\nLista de dados seleccionados")
    for i, dado in enumerate(dados_usuario):
        print("{}. [{}]".format(i + 1, tipos_de_dados[dado]))

# Lanza los dados seleccionados y muestra los resultados
def lanzar_dados(dados_usuario, tipos_de_dados):
    system("cls")
    print("\nLanzando los dados:")
    resultados_dados_usuario = []
    for dado in dados_usuario:
        caras = {1: 6, 2: 4, 3: 8, 4: 10, 5: 12, 6: 120}
        resultado_dado = randint(1, caras[dado])
        resultados_dados_usuario.append(resultado_dado)
    mostrar_resultados_dados_usuario(dados_usuario, resultados_dados_usuario, tipos_de_dados)

# Muestra los resultados de lanzar los dados
def mostrar_resultados_dados_usuario(dados_usuario, resultados_dados_usuario, tipos_de_dados):
    for i in range(len(dados_usuario)):
        dado = tipos_de_dados[dados_usuario[i]]
        resultado_dado = resultados_dados_usuario[i]
        print("{}. [{}]: {}".format(i + 1, dado, resultado_dado))

# Inicia el juego de dados
def iniciar_juego():
    mensaje_bienvenida()
    solicitar_dado_usuario()

# Inicia el juego
if __name__ == "__main__":
    iniciar_juego()

# Marc Delgado Ferreres