### Bucle For ###

# Qué función tiene #

# El bucle "for" utiliza para iterar sobre una secuencia de elementos, como una lista, una cadena de texto o un rango de números. 
# Permite ejecutar un bloque de código repetidamente para cada elemento de la secuencia.

# Ejemplo 1 #

mensaje = "Hola, mundo!"

for caracter in mensaje:
    print(caracter)

# En este ejemplo, se utiliza el bucle "for" para iterar sobre cada caracter de la cadena de texto "Hola, mundo!".
# En cada iteración, se imprime el caracter en la consola.
# El resultado será imprimir cada caracter de la cadena en líneas separadas:
# H
# o
# l
# a
# ,
#  
# m
# u
# n
# d
# o
# !

# Ejemplo 2 #

# Podemos observar en el ejemplo que se usa el "range()" para forzar generar un rango etre dos números.

for i in range(1, 6):
    print(i)

# En este ejemplo, se utiliza el bucle "for" para iterar sobre un rango de números del 1 al 5.
# En cada iteración, se imprime el número en la consola.
# El resultado será imprimir los números del 1 al 5 en líneas separadas:
# 1
# 2
# 3
# 4
# 5

# Marc Delgado Ferreres