### Listas ###

# Qué función tienen #

# Las listas en Python son estructuras de datos que permiten almacenar múltiples elementos en un solo lugar. 
# Cada elemento en una lista tiene una posición o índice que comienza desde 0.
# Las listas son útiles para almacenar colecciones de elementos relacionados, como números, cadenas de texto u otros objetos.

# Lista de números #

numeros = [1, 2, 3, 4, 5]
print(numeros)

# Se imprimirá:
# [1, 2, 3, 4, 5]

# Lista de vocales #

vocales = ["a", "e", "i", "o", "u"]
print(vocales)

# Se imprimirá:
# ["a", "e", "i", "o", "u"]

# Lista de diferentes tipos de datos #

datos_diferentes = ["manzana", 240, True]
print(datos_diferentes)

# Se imprimirá:
# ["manzana", 240, True]

# Lista vacía #

lista_vacia = []
print(lista_vacia)  

# Se imprimirá:
# []

# Acceder a elementos de la lista #

indice_cero_numeros = numeros[0]
indice_uno_vocales = vocales[1]
indice_dos_datos_diferentes = datos_diferentes[2]
print(indice_cero_numeros)
print(indice_uno_vocales)
print(indice_dos_datos_diferentes)

# Se utilizan los índices para acceder a un elemento dentro de una lista.
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

# Se utilizan los índices negativos para acceder a un elemento de adelante hacia atrás.
# El índice -1 corresponde al último elemento, el índice -2 corresponde al penúltimo elemento, etc.
# Los valores se asignan a las variables "indice_uno_negativo_numeros", "indice_dos_negativo_vocales" y "indice_tres_negativo_datos_diferentes".
# Se imprimirá:
# 5
# o
# manzana

# Modificar elementos de la lista #

numeros[2] = 10
print(numeros)

# Se modifica el elemento en el índice 2 de la lista "numeros" y se asigna el valor 10.
# Se imprimirá:
# [1, 2, 10, 4, 5]

# Obtener la longitud de la lista #

longitud = len(numeros)
print(longitud)

# Se utiliza la función "len()" para obtener la cantidad de elementos de la lista "numeros".
# El valor de la longitud se asigna a la variable "longitud".
# Se imprimirá:
# 5

# Crear una lista a partir de un rango #

range_list = list(range(0,21,2))
print(range_list)

# Generar una lista de números pares del 0 al 20 utilizando la función "range()"
# Luego convertirla en una lista con "list()".
# Se imprimirá:
# ["0", "2", "4", "6", "8", "10", "12", 14", "16", "18", "20"]

# Rebanadas #

alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
print(alfabeto)

# Podemos acceder a un rango de elementos en una lista utilizando la notación de rebanadas.
# Esto nos ayuda a seleccionar una parte específica de una lista creando una nueva.

alfabeto_a_j = alfabeto[0:11]
print(alfabeto_a_j)

# Obtiene una lista con los elementos desde el índice 0, que contiene el elemento "a", hasta el índice 11, que representa el elemento "k".
# El ultimo elemento nunca se añade a la nueva lista.
# Se imprimirá:
# ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

alfabeto_q_x = alfabeto[-10:-2]
print(alfabeto_q_x)

# Obtiene una lista con los elementos desde el índice -10, que contiene el elemento "q", hasta el índice -2, que representa el elemento "y".
# El ultimo elemento nunca se añade a la nueva lista.
# Se imprimirá:
# ["q", "r", "s", "t", "u", "v", "w", "x"]

alfabeto_inverso = alfabeto[::-1]
print(alfabeto_inverso)

# Obtiene una lista con los elementos de la lista original ordenados de forma inversa.
# Se imprimirá:
# ["z", "y", "x", "w", "v", "u", "t", "s", "r", "q", "p", "o", "n", "m", "l", "k", "j", "i", "h", "g", "f", "e", "d", "c", "b", "a"]

# Funciones en listas #

# Para trabajar eficientemente con listas, existen diversas funciones dedicadas.
# Estas funciones te permiten realizar acciones como agregar, eliminar, ordenar y acceder a elementos en una lista. 
# Estas funciones facilitan la manipulación de listas y la realización de operaciones comunes.

# Creamos una función de prueba #

lista_prueba = ["a", "b", "a", "c", "c", "e", "e"]
print(lista_prueba)

# Función "append()" #

# Agregar un elemento al final de la lista.

lista_prueba.append("f")
print(lista_prueba)

# Agrega "e" al final de la lista.
# Se imprimirá:
# ["a", "b", "a", "c", "c", "e", "e", "f"]

# Función "insert()" #

# Insertar un elemento en una posición específica.

lista_prueba.insert(5, "d")  
print(lista_prueba)  

# Insertar el elemento "d" en el índice 4.
# Se imprimirá:
# ["a", "b", "a", "c", "c", "d", "e", "e", "f"]

# Función "remove()" #

# Eliminar el primer elemento con un valor específico.

lista_prueba.remove("e")  
print(lista_prueba)  

# Eliminar el primer elemento "e".
# Se imprimirá:
# ["a", "b", "a", "c", "c", "d", "e", "f"]

# Función "pop()" #

# Elimina y devuelve el elemento en un índice específica. 
# Si no se proporciona un índice, elimina el último elemento.

valor_eliminado = lista_prueba.pop(4)  
print(valor_eliminado)
print(lista_prueba)

# Eliminar el índice 4 y guarda su valor.
# Se imprimirá:
# c
# ["a", "b", "a", "c", "d", "e", "f"]

valor_eliminado = lista_prueba.pop()  
print(valor_eliminado)
print(lista_prueba)

# Eliminar el último índice y guarda su valor.
# Se imprimirá:
# f
# ["a", "b", "a", "c", "d", "e"]

# Función "index()" #

# Buscar el índice del primer elemento con un valor específico.

indice = lista_prueba.index("a")  
print(indice)  

# Obtener el primer índice del elemento "a".
# Se imprimirá:
# 0

# Función "count()" #

# Contar la cantidad de veces que aparece un elemento en la lista.

cantidad = lista_prueba.count("a")  
print(cantidad)  

# Contar cuántas veces aparece el elemento "d".
# Se imprimirá:
# 2

# Función "sort()" #

# Ordenar la lista de forma ascendente.

lista_prueba.sort()  
print(lista_prueba)  

# Se imprimirá:
# ["a", "a", "b", "c", "d", "e"]

# Ordenar la lista de forma descendente.

lista_prueba.sort(reverse=True)  
print(lista_prueba)  

# Se imprimirá:
# ["e", "d", "c", "b", "a", "a"]

# Función "copy()" #

# Crear una copia de la lista.

lista_copia = lista_prueba.copy()  
print(lista_copia)  

# Se imprimirá:
# ["e", "d", "c", "b", "a", "a"]

# Función "clear()" #

# Vaciar la lista.

lista_prueba.clear()  
print(lista_prueba)  

# Se imprimirá:
# []

# Función "extend()" #

# Extender una lista con los elementos de otra lista.

lista_prueba.extend([1, 2, 3])  
print(lista_prueba)  

# Se imprimirá:
# [1, 2, 3]

lista_prueba.extend([4, 5, 6])  
print(lista_prueba)  

# Se imprimirá:
# [1, 2, 3, 4, 5, 6]

# Listas dimensionales #

# Es posible crear una lista cuyos elementos sean otras listas.
# A esto se le conoce como lista dimensional.

# Crear lista dimensional #

lista_dimensional = [["1", "2", "3", "4"], ["a", "b", "c", "d"], ["A", "B", "C", "D"]]
print(lista_dimensional)

# Se imprimirá:
# [["1", "2", "3", "4"], ["a", "b", "c", "d"], ["A", "B", "C", "D"]]

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

# Modificar elementos de la lista dimensional #

lista_dimensional[1][-1] = "hola"
print(lista_dimensional)

# Se modifica el elemento con el índice -1 de la lista con el índice 1 la lista "lista_dimensional" y se asigna el valor "hola".
# Se imprimirá:
# [["1", "2", "3", "4"], ["a", "b", "c", "hola"], ["A", "B", "C", "D"]]

# Marc Delgado Ferreres