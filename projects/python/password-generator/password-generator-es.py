# Importar las funciones ascii_letters, digits y punctuation del módulo string
from string import ascii_letters, digits, punctuation

# Importar la función choice del módulo random
from random import choice

# Esta función permite al usuario configurar las opciones de contraseña (letras, números, símbolos).
def ajustes_contraseña():
    letras = False
    numeros = False
    simbolos = False
    while True:
        print("Opciones de contraseña:\n")
        print("1. [{}] Letras (Aa)".format("Sí" if letras else "No"))
        print("2. [{}] Dígitos (123)".format("Sí" if numeros else "No"))
        print("3. [{}] Símbolos (@&$!#?)".format("Sí" if simbolos else "No"))
        print("4. Continuar...") 
        try:
            opcion = int(input("\nSelecciona una opción (1/2/3/4): "))
            
            if opcion == 1:
                letras = not letras
            elif opcion == 2:
                numeros = not numeros
            elif opcion == 3:
                simbolos = not simbolos
            elif opcion == 4:
                break
            else:
                print("ERROR: Debes seleccionar una opción válida (1/2/3/4).\n")
        except ValueError:
            print("ERROR: Debes seleccionar una opción válida (1/2/3/4).\n")
    return letras, numeros, simbolos

# Esta función permite al usuario configurar la longitud deseada de la contraseña.
def ajustes_longitud():
    while True:
        try:
            longitud = int(input("\nLongitud de la contraseña (4-100): "))
            if 4 <= longitud <= 100:
                return longitud
            else:
                print("ERROR: La longitud debe estar en el rango de 4 a 100 caracteres.")
        except ValueError:
            print("ERROR: Debes ingresar un número entero válido para la longitud.\n")

# Esta función genera una contraseña basada en las opciones seleccionadas por el usuario.
def generar_contraseña(letras, numeros, simbolos, longitud):
    abecedario_contraseña = ""
    if letras:
        abecedario_contraseña += ascii_letters
    if numeros:
        abecedario_contraseña += digits
    if simbolos:
        abecedario_contraseña += punctuation
    if not abecedario_contraseña:
        print("ERROR: Debes seleccionar al menos un tipo de carácter (letras, números o símbolos) para generar la contraseña.\n")
        return
    contraseña = ''.join(choice(abecedario_contraseña) for _ in range(longitud))
    print("\nContraseña generada: {}".format(contraseña))

# Esta función inicia el programa principal.
def iniciar_programa():
    print("Generador de Contraseñas\n")
    letras, numeros, simbolos = ajustes_contraseña()
    longitud = ajustes_longitud()
    generar_contraseña(letras, numeros, simbolos, longitud)

# Iniciar el programa
if __name__ == "__main__":
    iniciar_programa()

# Marc Delgado Ferreres