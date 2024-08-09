### Excepciones ###

# Qué función tiene #

# Las excepciones, junto con las declaraciones "try" y "except", se utilizan para manejar errores y situaciones excepcionales durante la ejecución de un programa.

# Try #

# La función principal del bloque "try" es intentar ejecutar un bloque de código en el que se sospecha que puede ocurrir una excepción. 
# Dentro del bloque try, se coloca el código que puede generar una excepción.

# Except #

# La función del bloque "except" es capturar y manejar las excepciones que ocurren dentro del bloque try. 
# Si ocurre una excepción dentro del bloque try, el programa buscará un bloque except correspondiente que pueda manejar esa excepción en particular. 
# El bloque except contiene el código que se ejecutará cuando se capture la excepción.

# Ejemplo 1 #

try:
    primer_numero = 10
    segundo_numero = 10
    resultado = primer_numero // segundo_numero
    print("El resultado de la división entera es: {}".format(resultado))
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero")
except NameError:
    print("Error: Variable no definida")

# En este ejemplo, se utiliza el bloque "try" para ejecutar el código que realiza una división entera entre dos números ingresados por el usuario.
# Como no hay ningún error el bloque "try" funciona perfectamente. El programa imprime: 
# El resultado de la división es: 1

# Ejemplo 2 #

try:
    primer_numero = 10
    segundo_numero = 0
    resultado = primer_numero / segundo_numero
    print("El resultado de la división entera es: {}".format(resultado))
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero")
except NameError:
    print("Error: Variable no definida")

# En este ejemplo, se utiliza el bloque "try" para ejecutar el código que realiza una división entera entre dos números ingresados por el usuario.
# Como hay un error "ZeroDivisionError" el bloque "try" no funciona. El programa imprime: 
# Error: No se puede dividir entre cero

# Ejemplo 3 #

try:
    primer_numero = numero
    segundo_numero = 10
    resultado = primer_numero / segundo_numero
    print("El resultado de la división entera es: {}".format(resultado))
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero")
except NameError:
    print("Error: Variable no definida")

# En este ejemplo, se utiliza el bloque "try" para ejecutar el código que realiza una división entera entre dos números ingresados por el usuario.
# Como hay un error "NameError" el bloque "try" no funciona. El programa imprime: 
# Error: Variable no definida

# Marc Delgado Ferreres