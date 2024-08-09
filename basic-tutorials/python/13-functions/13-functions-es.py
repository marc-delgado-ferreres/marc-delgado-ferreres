### Funciones ###

# Qué función tienen #

# Las funciones en Python son bloques de código reutilizables que realizan una tarea específica.
# Permiten organizar y modularizar el código, evitando la repetición y mejorando la legibilidad.
# Las funciones se definen utilizando la palabra clave "def", seguida del nombre de la función y sus parámetros.

# Definir una función #

def saludar(nombre):
    print("Hola, {}!".format(nombre))

# Llamar a una función #

saludar("Juan")
saludar("María")

# Se define la función "saludar" que toma un parámetro "nombre" e imprime un saludo personalizado.
# Luego se llaman a la función dos veces con diferentes nombres.
# Se imprimirá:
# Hola, Juan!
# Hola, María!

# Parámetros y argumentos #

def suma(a, b):
    resultado = a + b
    return resultado

resultado_suma = suma(5, 3)
print(resultado_suma)

# Se define la función "suma" que toma dos parámetros "a" y "b", suma los valores y devuelve el resultado.
# Luego se llama a la función con los argumentos 5 y 3, y se imprime el resultado.
# Se imprimirá:
# 8

# Parámetros predeterminados #

def saludar(nombre="Usuario"):
    print("Hola, {}!".format(nombre))

saludar()
saludar("Juan")

# Se define la función "saludar" con un parámetro predeterminado "nombre" que es "Usuario".
# Luego se llama a la función dos veces, una sin argumentos y otra con el argumento "Juan".
# Se imprimirá:
# Hola, Usuario!
# Hola, Juan!

# Pasar argumentos por posición y por nombre #

def presentar(nombre, edad):
    print("Mi nombre es {} y tengo {} años.".format(nombre, edad))

presentar("Juan", 30)
presentar(edad=25, nombre="María")

# Se define la función "presentar" que toma dos parámetros "nombre" y "edad".
# Luego se llama a la función dos veces, una pasando argumentos por posición y otra por nombre.
# Se imprimirá:
# Mi nombre es Juan y tengo 30 años.
# Mi nombre es María y tengo 25 años.

# Retorno de múltiples valores #

def dividir(numero1, numero2):
    cociente = numero1 // numero2
    residuo = numero1 % numero2
    return cociente, residuo

cociente, residuo = dividir(10, 3)
print("Cociente: {}, Residuo: {}".format(cociente, residuo))

# Se define la función "dividir" que toma dos números y devuelve el cociente y el residuo de la división.
# Luego se llama a la función con los números 10 y 3, y se desempaquetan los valores en las variables "cociente" y "residuo".
# Se imprimirá:
# Cociente: 3, Residuo: 1

# Funciones lambda #

doble = lambda x: x * 2

resultado_doble = doble(4)
print(resultado_doble)

# Se define una función lambda (anónima) que multiplica un número por 2.
# Luego se llama a la función con el número 4 y se imprime el resultado.
# Se imprimirá:
# 8

# Funciones predefinidas #

# En Python existen numerosas funciones predefinidas en la biblioteca estándar que se pueden utilizar directamente.

# Lista de funciones predefinidas #

# Existe una gran infinidad de funciones en la biblioteca estandar de Python.
# Algunas de las funciones más utilizadas són las siguientes:

# - abs(): devuelve el valor absoluto de un número.
# - ascii(): devuelve una representación con escape de un objeto usando caracteres "ascii".
# - bin(): convierte un número entero a su representación binaria.
# - bool(): convierte un valor a un valor booleano.
# - chr(): convierte un valor "unicode" a su caracter correspondiente.
# - float(): convierte un valor a un número de punto flotante.
# - format(): formatea una cadena de caracteres con valores.
# - hex(): convierte un número entero a su representación hexadecimal.
# - input(): lee una línea de entrada desde la consola.
# - int(): convierte un valor a un entero.
# - len(): devuelve la longitud de un objeto (cadena, lista, tupla, etc.).
# - list(): crea una lista a partir de un iterable.
# - max(): devuelve el valor máximo en un iterable.
# - min(): devuelve el valor mínimo en un iterable.
# - oct(): convierte un número entero a su representación octal.
# - open(): abre un archivo en diferentes modos.
# - ord(): convierte un carácter "unicode" a su valor entero correspondiente.
# - print(): imprime valores en la consola.
# - range(): genera una secuencia de números enteros.
# - reversed(): devuelve un iterador invertido de un iterable.
# - round(): redondea un número a una cantidad específica de decimales.
# - slice(): crea un objeto de rebanada para indexar secuencias.
# - sorted(): ordena elementos en un iterable.
# - str(): convierte un valor a una cadena de caracteres.
# - sum(): calcula la suma de elementos en un iterable.
# - tuple(): crea una tupla a partir de un iterable.
# - type(): devuelve el tipo de un objeto.

# Marc Delgado Ferreres