### Diccionarios ###

# Qué función tienen #

# Los diccionarios en Python son estructuras de datos que permiten almacenar pares clave-valor.
# Cada elemento en un diccionario se almacena junto con su clave correspondiente y su valor asociado.
# Los diccionarios son útiles para representar información que se organiza en pares clave-valor.

# Diccionario de información de personas #

persona = {
    "nombre": "Juan",
    "edad": 30,
    "profesion": "ingeniero"
}
print(persona)

# Se imprimirá:
# {'nombre': 'Juan', 'edad': 30, 'profesion': 'ingeniero'}

# Acceder a elementos del diccionario #

nombre_persona = persona["nombre"]
edad_persona = persona["edad"]
profesion_persona = persona["profesion"]
print(nombre_persona)
print(edad_persona)
print(profesion_persona)

# Se utilizan las claves para acceder a los valores correspondientes en el diccionario.
# Los valores se asignan a las variables "nombre_persona", "edad_persona" y "profesion_persona".
# Se imprimirá:
# Juan
# 30
# ingeniero

# Modificar elementos del diccionario #

persona["edad"] = 31
print(persona)

# Se modifica el valor asociado a la clave "edad" en el diccionario "persona".
# Se imprimirá:
# {'nombre': 'Juan', 'edad': 31, 'profesion': 'ingeniero'}

# Agregar elementos al diccionario #

persona["ciudad"] = "Madrid"
print(persona)

# Se agrega un nuevo par clave-valor al diccionario "persona".
# Se imprimirá:
# {'nombre': 'Juan', 'edad': 31, 'profesion': 'ingeniero', 'ciudad': 'Madrid'}

# Eliminar elementos del diccionario #

del persona["profesion"]
print(persona)

# Se elimina el par clave-valor asociado a la clave "profesion" en el diccionario "persona".
# Se imprimirá:
# {'nombre': 'Juan', 'edad': 31, 'ciudad': 'Madrid'}

# Funciones en diccionarios #

# Para trabajar con diccionarios, existen diversas funciones dedicadas.
# Estas funciones te permiten realizar acciones como obtener claves, valores y pares clave-valor.

# Crear una copia del diccionario #

persona_copia = persona.copy()
print(persona_copia)

# Se crea una copia del diccionario "persona".
# Se imprimirá:
# {'nombre': 'Juan', 'edad': 31, 'ciudad': 'Madrid'}

# Obtener una lista de todas las claves #

claves = persona.keys()
print(claves)

# Se obtiene una lista de todas las claves en el diccionario "persona".
# Se imprimirá:
# dict_keys(['nombre', 'edad', 'ciudad'])

# Obtener una lista de todos los valores #

valores = persona.values()
print(valores)

# Se obtiene una lista de todos los valores en el diccionario "persona".
# Se imprimirá:
# dict_values(['Juan', 31, 'Madrid'])

# Obtener una lista de todos los pares clave-valor #

items = persona.items()
print(items)

# Se obtiene una lista de todos los pares clave-valor en el diccionario "persona".
# Se imprimirá:
# dict_items([('nombre', 'Juan'), ('edad', 31), ('ciudad', 'Madrid')])

# Marc Delgado Ferreres