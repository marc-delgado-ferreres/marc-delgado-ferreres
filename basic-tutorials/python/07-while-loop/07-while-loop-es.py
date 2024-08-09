### Bucle While ###

# Qué función tiene #

# El bucle "while" se utiliza para repetir un bloque de código mientras se cumpla una condición.
# Permite ejecutar el bloque de código repetidamente hasta que la condición se evalúe como "False".

# Ejemplo 1 #

contador = 0

while contador < 5:
    print("Contador:", contador)
    contador += 1

# En este ejemplo, se utiliza el bucle "while" para repetir un bloque de código mientras la variable "contador" sea menor que 5.
# En primer lugar, se evalúa la condición "contador < 5" y si esta es "True", se ejecuta el bloque de código dentro del bucle "while".
# Si la condición se cumple, la condición se evalúa como "True" y el bucle se repite mientras esta condición continúe siendo "True". 
# Si la condición no se cumple, la condición se evalúa como "False" y el bucle se detiene.
# Como resultado, se imrpime el valor del contador en cada iteración, desde 0 hasta 4:
# Contador: 0
# Contador: 1
# Contador: 2
# Contador: 3
# Contador: 4

# Ejemplo 2 #

primero = 0
segundo = 1
print("Contador: {}".format(primero))
print("Contador: {}".format(segundo))

while True:
    resultado = primero + segundo
    print("Contador: {}".format(resultado))
    primero = segundo
    segundo = resultado

# En este ejemplo, se utiliza el bucle "while" para repetir un bloque de código de forma indefinida, recreando la secuencia de fibonacci.
# En primer lugar, se evalúa la condición "True" y se ejecuta el bloque de código dentro del bucle "while".
# Si la condición se cumple, la condición se evalúa como "True" y el bucle se repite mientras esta condición continúe siendo "True". 
# Como la condición siempre es "True" este bloque de código se repite de forma indefinida.
# Como resultado, primero se imprime el valor de las variables "primero" y "segundo" y después se imprime la suma del último y penúltimo valor imprimidos de forma indefinida:
# Contador: 0
# Contador: 1
# Contador: 1
# Contador: 2
# Contador: 3
# Contador: 5
# Contador: 8
# Contador: 13
# Contador: 21
# Contador: 34
# Contador: 55
# Contador: 89
# Contador: 144
# Contador: 233
# Contador: 377
# Contador: 610
# Contador: 987
# Contador: 1597
# Contador: 2584
# ...

# Tenga cuidado con la creación de códigos indefinidos, ya que estos pueden causar muchos problemas si el código está mal programado.

# Marc Delgado Ferreres