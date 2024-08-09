### Estructura de Control ###

# Qué función tiene #

# Los condicionales "if" y "else" se utiliza para tomar decisiones basadas en una condición.
# Permite ejecutar un bloque de código si la condición es verdadera y otro bloque de código si la condición es falsa.

# If #

# El condicional "if" se utiliza para ejecutar un bloque de código si una condición es verdadera.
# El bloque de código dentro del "if" se ejecuta solo si la condición se cumple. Si la condición no se cumple, se salta el bloque "if".

if False == True:
    print("False == True is True")
if True == False:
    print("True == False is True")
if True == True:
    print("True == True is True")
if False == False:
    print("False == False is True")

# En este ejemplo, podemos observar cuatro condicionales "if" seguidos.
# El primer y el segundo condicional "if" no se cumplen, por tanto, no se activan los bloques respectivos.
# El tercer condicional "if" se cumple, por tanto, se activa el bloque respectivo y se imprime: "True == True is True".
# El cuarto condicional "if" se cumple, por tanto, se activa el bloque respectivo y se imprime "False == False is True".

# Else #

# El condicional "else" se utiliza en combinación con el "if" para proporcionar un bloque de código alternativo que se ejecuta cuando la condición del "if" no se cumple.
# El bloque de código dentro del "else" se ejecuta solo si la condición del "if" no se cumple.

if False == True:
    print("False == True is True")
if True == False:
    print("True == False is True")
else:
    print("Descarte")

# En este ejemplo, podemos observar tres condicionales, dos condicionales "if" y un condicional "else".
# El primer y el segundo condicional "if" no se cumplen, por tanto, no se activan los bloques respectivos.
# El tercer condicional "else" se activa por descarte, por tanto, se activa el bloque respectivo y se imprime "Descarte".

# Elif #

# El condicional "elif" es una abreviatura de "else if" y se utiliza para comprobar múltiples condiciones en secuencia.
# Se puede utilizar después del "if" o de otro "elif" para proporcionar bloques de código adicionales que se ejecutan cuando se cumplen ciertas condiciones.
# Solo se ejecutará el bloque de código correspondiente a la primera condición que se cumpla.

if False == True:
    print("False == True is True")
elif True == False:
    print("True == False is True")
elif True == True:
    print("True == True is True")
elif False == False:
    print("False == False is True")

# En este ejemplo, podemos observar cuatro condicionales, un condicional "if" y tres condicionales "elif".
# El primer condicional "if" no se cumple, por tanto, no se activa el bloque respectivo.
# El segundo condicional "elif" no se cumple, por tanto, no se activa el bloque respectivo.
# El tercer condicional "elif" se cumple, por tanto, se activa el bloque respectivo y se imprime "True == True is True".
# El cuarto condicional "elif" no se activa debido a que ya ha habido un bloque que se ha activado y el restante es un condicional "elif".

# Marc Delgado Ferreres