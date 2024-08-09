### Tuplas ###

# Qué función tienen #

# Las tuplas en Python son estructuras de datos similares a las listas, pero cson inmutables.
# Esto significa que una vez que se crea una tupla, no se pueden modificar sus elementos.
# Las tuplas se utilizan para almacenar colecciones ordenadas de elementos, al igual que las listas,
# Son útiles para almacenar datos que no deben cambiarse.

# Tupla de números #

numeros = (1, 2, 3, 4, 5)
print(numeros)

# Se imprimirá:
# (1, 2, 3, 4, 5)

# Tupla de vocales #

vocales = ("a", "e", "i", "o", "u")
print(vocales)

# Se imprimirá:
# ("a", "e", "i", "o", "u")

# Tupla de diferentes tipos de datos #

datos_diferentes = ("manzana", 240, True)
print(datos_diferentes)

# Se imprimirá:
# ("manzana", 240, True)

# Tupla vacía #

tupla_vacia = ()
print(tupla_vacia)  

# Se imprimirá:
# ()

# Acceder a elementos de la tupla #

indice_cero_numeros = numeros[0]
indice_uno_vocales = vocales[1]
indice_dos_datos_diferentes = datos_diferentes[2]
print(indice_cero_numeros)
print(indice_uno_vocales)
print(indice_dos_datos_diferentes)

# Se utilizan los índices para acceder a un elemento dentro de una tupla.
# El índice 0 corresponde al primer elemento, el índice 1 corresponde al segundo elemento, etc.
# Los valores se asignan a las variables "indice_cero_numeros", "indice_uno_vocales" y "indice_dos_datos_diferentes".
# Se imprimirá:
# 1
# e
# True

indice_uno_negativo_numeros = numeros[-1]
indice_dos_negativo_vocales = vocales[-2]
indice_tres_negativo_datos_diferentes = datos_diferentes[-3]
print(indice_uno_negativo_numeros)
print(indice_dos_negativo_vocales)
print(indice_tres_negativo_datos_diferentes)

# Se utilizan los índices negativo para acceder a un elemento de adelante hacia atrás.
# El índice -1 corresponde al último elemento, el índice -2 corresponde al penúltimo elemento, etc.
# Los valores se asignan a las variables "indice_uno_negativo_numeros", "indice_dos_negativo_vocales" y "indice_tres_negativo_datos_diferentes".
# Se imprimirá:
# 5
# o
# manzana

# Tuplas dimensionales #

# Es posible crear una lista cuyos elementos sean otras tuplas.
# A esto se le conoce como tupla dimensional.

# Crear tupla dimensional #

lista_dimensional = (("1", "2", "3", "4"), ("a", "b", "c", "d"), ("A", "B", "C", "D"))
print(lista_dimensional)

# Se imprimirá:
# (("1", "2", "3", "4"), ("a", "b", "c", "d"), ("A", "B", "C", "D"))

# Acceder a elementos de la lista dimensional #

indice_uno_indice_uno_lista_dimensional = lista_dimensional[0][0]
indice_dos_indice_dos_lista_dimensional = lista_dimensional[1][1]
indice_tres_indice_tres_lista_dimensional = lista_dimensional[2][2]
print(indice_uno_indice_uno_lista_dimensional)
print(indice_dos_indice_dos_lista_dimensional)
print(indice_tres_indice_tres_lista_dimensional)

# Se utilizan los índices para acceder a un elemento dentro de una lista.
# Para acceder a una lista dentro de la lista se utiliza un índice.
# Luego para acceder a un elemento dentro de la lista seleccionada se utiliza otro índice
# Los valores se asignan a las variables "indice_uno_indice_uno_lista_dimensional", "indice_dos_indice_dos_lista_dimensional" y "indice_tres_indice_tres_lista_dimensional".
# Se imprimirá:
# 1
# b
# C

indice_uno_negativo_indice_uno_negativo_lista_dimensional = lista_dimensional[-1][-1]
indice_dos_negativo_indice_dos_negativo_lista_dimensional = lista_dimensional[-2][-2]
indice_tres_negativo_indice_tres_negativo_lista_dimensional = lista_dimensional[-3][-3]
print(indice_uno_negativo_indice_uno_negativo_lista_dimensional)
print(indice_dos_negativo_indice_dos_negativo_lista_dimensional)
print(indice_tres_negativo_indice_tres_negativo_lista_dimensional)

# Se utilizan los índices negativos para acceder a un elemento de adelante hacia atrás.
# El índice -1 corresponde al último elemento, el índice -2 corresponde al penúltimo elemento, etc.
# Los valores se asignan a las variables "indice_uno_negativo_indice_uno_negativo_lista_dimensional", "indice_dos_negativo_indice_dos_negativo_lista_dimensional" y "indice_tres_negativo_indice_tres_negativo_lista_dimensional".
# Se imprimirá:
# D
# c
# 2

# Marc Delgado Ferreres