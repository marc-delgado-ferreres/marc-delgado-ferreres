### Bibliotecas ###

# Las bibliotecas en Python son colecciones de módulos y funciones que proporcionan funcionalidades adicionales.
# Estas funcionalidades van más allá de las funciones predefinidas en la biblioteca estándar.
# Para utilizar una biblioteca, primero debes importarla en tu código.

# Importar una biblioteca completa #

import math

# Importamos toda la biblioteca "math", que proporciona funciones matemáticas avanzadas.

# Importar funciones específicas #

from math import sqrt, radians

# Importamos las funciones "sqrt" y "radians" directamente desde la biblioteca "math".
# Esto nos permite usar estas funciones sin tener que escribir "math." antes de cada llamada.

# Importar con alias #

from math import ceil as redondear  

# Importamos la función "ceil" de la biblioteca "math" y le asignamos el alias "redondear".
# Ahora podemos llamar a la función usando "redondear" en lugar de "ceil".

# Uso de funciones de biblioteca #

# Ejemplo 1: Calcular la raíz cuadrada de un número
numero = 25
raiz_cuadrada = math.sqrt(numero)
print("La raíz cuadrada de", numero, "es:", raiz_cuadrada)

# Ejemplo 2: Calcular el seno de un ángulo en radianes
angulo_radianes = math.radians(30)
seno = math.sin(angulo_radianes)
print("El seno de", angulo_radianes, "radianes es:", seno)

# Ejemplo 3: Redondear un número hacia arriba
numero_decimal = 4.7
numero_redondeado_arriba = redondear(numero_decimal)
print("El número", numero_decimal, "redondeado hacia arriba es:", numero_redondeado_arriba)

# Lista de bibliotecas más famosas #

# - math: Proporciona funciones matemáticas avanzadas.
# - os: Proporciona funciones para interactuar con el sistema operativo.
# - datetime: Proporciona clases para trabajar con fechas y horas.
# - random: Proporciona funciones para generar números aleatorios.
# - requests: Se utiliza para realizar solicitudes HTTP.
# - numpy: Proporciona estructuras de datos y funciones para operaciones numéricas.
# - pandas: Proporciona estructuras de datos y herramientas para el análisis de datos.
# - matplotlib: Se utiliza para crear visualizaciones gráficas.
# - tensorflow: Biblioteca de aprendizaje automático y redes neuronales.
# - tkinter: Se utiliza para crear interfaces gráficas de usuario (GUI).

# Las bibliotecas pueden ampliar enormemente las capacidades de Python y simplificar el desarrollo de aplicaciones más complejas.

# Marc Delgado Ferreres