### Operadores ###

# Qué función tienen #

# Los operadores son símbolos especiales que se utilizan para realizar operaciones en variables y valores.
# Permiten realizar cálculos matemáticos, comparaciones y manipulaciones de datos.

# Operadores aritméticos #

# Las operaciones aritméticas son las operaciones matemáticas básicas que se utilizan para realizar cálculos numéricos

# Suma #

suma = 75 + 25
print(suma)

# El operador "+" se utiliza para sumar.
# El resultado se guarda en la variable "suma".
# Como resultado, el valor de "suma" será: 
# 100

suma += 100
print(suma)

# El operador "+=" se utiliza para sumarle a una variable un valor.
# El resultado se guarda en la variable "suma".
# Como resultado, el valor de "suma" será:
# 200

# Resta #

resta = 125 - 25
print(resta)

# El operador "-" se utiliza para restar.
# El resultado se guarda en la variable "resta".
# Como resultado, el valor de "resta" será: 
# 100

resta -= 100
print(resta)

# El operador "-=" se utiliza para restarle a una variable un valor.
# El resultado se guarda en la variable "resta".
# Como resultado, el valor de "resta" será: 
# 0

# Multiplicación #

multiplicacion = 4 * 25
print(multiplicacion)

# El operador "*" se utiliza para multiplicar.
# El resultado se guarda en la variable "multiplicacion".
# Como resultado, el valor de "multiplicacion" será:
# 100

multiplicacion *= 2
print(multiplicacion)

# El operador "*=" se utiliza para multiplicarle a una variable un valor.
# El resultado se guarda en la variable "multiplicacion".
# Como resultado, el valor de "multiplicacion" será: 
# 200

# División #

# Cuando realizas una division, el resultado de dicha operación será siempre de tipo flotante.

division = 2500 / 25
print(division)

# El operador "/" se utiliza para dividir.
# El resultado se guarda en la variable "division".
# Como resultado, el valor de "division" será:
# 100.0

division /= 4
print(division)

# El operador "/=" se utiliza para dividirle a una variable un valor.
# El resultado se guarda en la variable "division".
# Como resultado, el valor de "division" será:
# 25.0

# División entera #

# Cuando realizas una division entera, el resultado devuelve solo la parte entera del resultado, descartando cualquier parte decimal.

division_entera = 200 // 12
print(division_entera)

# El operador "//" se utiliza para dividir.
# El resultado se guarda en la variable "division_entera".
# Como resultado, el valor de "division_entera" será:
# 16

division_entera //= 2
print(division_entera)

# El operador "/=" se utiliza para dividirle a una variable un valor.
# El resultado se guarda en la variable "division_entera".
# Como resultado, el valor de "division_entera" será:
# 8

# Módulo #

modulo = 120 % 25
print(modulo)

# El operador "%" se utiliza para obtener el resto de la división.
# El resultado se guarda en la variable "modulo".
# Como resultado, el valor de "modulo" será:
# 25

modulo %= 15
print(modulo)

# El operador "%=" se utiliza para obtener el resto de la divisirle a una variable un valor.
# El resultado se guarda en la variable "modulo".
# Como resultado, el valor de "modulo" será:
# 5

# Operadores de comparación #

# Las operaciones de comparación se utilizan para comparar dos valores o variables y evaluar se cumple una determinada condición. 
# Estas operaciones devuelven un valor booleano que indica si la condición es verdadera o falsa.

# Igualdad #

# El operador "==" se utiliza para comparar si los valores son iguales.

igualdad = (100 == 25)
print(igualdad)

# El resultado se guarda en la variable "igualdad".
# Como resultado, el valor de "igualdad" será "False".

igualdad = (100 == 100)
print(igualdad)

# El resultado se guarda en la variable "igualdad".
# Como resultado, el valor de "igualdad" será "True".

# Mayor que o Menor que #

# El operador ">" se utiliza para comparar si el primer valor es mayor que el segundo.

mayor_que_menor_que = (10 > 25)
print(mayor_que_menor_que)

# El resultado se guarda en la variable "mayor_que_menor_que".
# Como resultado, el valor de "mayor_que_menor_que" será False.

mayor_que_menor_que = (25 > 10)
print(mayor_que_menor_que)

# El resultado se guarda en la variable "mayor_que_menor_que".
# Como resultado, el valor de "mayor_que_menor_que" será True.

# El operador "<" se utiliza para comparar si el segundo valor es mayor que el primero.

mayor_que_menor_que = (25 < 10)
print(mayor_que_menor_que)

# El resultado se guarda en la variable "mayor_que_menor_que".
# Como resultado, el valor de "mayor_que_menor_que" será False.

mayor_que_menor_que = (10 < 25)
print(mayor_que_menor_que)

# El resultado se guarda en la variable "mayor_que_menor_que".
# Como resultado, el valor de "mayor_que_menor_que" será True.

# Mayor o igual que o Menor o igual que #

# El operador ">=" se utiliza para comparar si el primer valor es mayor o igual que el segundo.

mayor_o_igual_que_menor_o_igual_que = (10 >= 25)
print(mayor_o_igual_que_menor_o_igual_que)

# El resultado se guarda en la variable "mayor_o_igual_que_menor_o_igual_que".
# Como resultado, el valor de "mayor_o_igual_que_menor_o_igual_que" será False.

mayor_o_igual_que_menor_o_igual_que = (25 >= 10)
print(mayor_o_igual_que_menor_o_igual_que)

# El resultado se guarda en la variable "mayor_o_igual_que_menor_o_igual_que".
# Como resultado, el valor de "mayor_o_igual_que_menor_o_igual_que" será True.

mayor_o_igual_que_menor_o_igual_que = (25 >= 25)
print(mayor_o_igual_que_menor_o_igual_que)

# El resultado se guarda en la variable "mayor_o_igual_que_menor_o_igual_que".
# Como resultado, el valor de "mayor_o_igual_que_menor_o_igual_que" será True.

# El operador "<=" se utiliza para comparar si el segundo valor es mayor o igual que el primero.

mayor_o_igual_que_menor_o_igual_que = (25 <= 10)
print(mayor_o_igual_que_menor_o_igual_que)

# El resultado se guarda en la variable "mayor_o_igual_que_menor_o_igual_que".
# Como resultado, el valor de "mayor_o_igual_que_menor_o_igual_que" será False.

mayor_o_igual_que_menor_o_igual_que = (10 <= 25)
print(mayor_o_igual_que_menor_o_igual_que)

# El resultado se guarda en la variable "mayor_o_igual_que_menor_o_igual_que".
# Como resultado, el valor de "mayor_o_igual_que_menor_o_igual_que" será True.

mayor_o_igual_que_menor_o_igual_que = (25 <= 25)
print(mayor_o_igual_que_menor_o_igual_que)

# El resultado se guarda en la variable "mayor_o_igual_que_menor_o_igual_que".
# Como resultado, el valor de "mayor_o_igual_que_menor_o_igual_que" será True.

# Diferente de #

# El operador "!=" se utiliza para comparar si los valores son distintos.

distinto_de = (25 != 25)

# El resultado se guarda en la variable "distinto_de".
# Como resultado, el valor de "distinto_de" será False.

distinto_de = (25 != 10)

# El resultado se guarda en la variable "distinto_de".
# Como resultado, el valor de "distinto_de" será True.

# Operadores lógicos #

# Las operaciones lógicas se utilizan para combinar o modificar expresiones lógicas y evaluar condiciones complejas. 

# And lógico #

# El operador "and" se utiliza para evaluar si ambas expresiones son verdaderas.

and_logico = False and False

# En este ejemplo, la expresión "False and False" se evalúa.
# Como resultado, la variable "and_logico" será False, ya que ambas expresiones no son verdaderas.

and_logico = True and False

# En este ejemplo, la expresión "True and False" se evalúa.
# Como resultado, la variable "and_logico" será False, ya que ambas expresiones no son verdaderas.

and_logico = True and True

# En este ejemplo, la expresión "True and True" se evalúa.
# Como resultado, la variable "and_logico" será True, ya que ambas expresiones son verdaderas.

# Or lógico #

# El operador "or" se utiliza para evaluar si al menos una de las expresiones es verdadera.

or_logico = False and False

# En este ejemplo, la expresión "False and False" se evalúa.
# Como resultado, la variable "or_logico" será False, ya que no hay al menos una de las expresiones que sea verdadera.

or_logico = True or False

# En este ejemplo, la expresión "True or False" se evalúa.
# Como resultado, la variable "or_logico" será True, ya que al menos una de las expresiones es verdadera.

or_logico = True and True

# En este ejemplo, la expresión "True and True" se evalúa.
# Como resultado, la variable "or_logico" será True, ya que al menos una de las expresiones es verdadera.

# Not lógico

# El operador "not" se utiliza para negar el valor de una expresión.

not_logico = not True

# En este ejemplo, la expresión "not True" se evalúa.
# Como resultado, la variable "not_logico" será False, ya que se niega el valor verdadero "True".

not_logico = not False

# En este ejemplo, la expresión "not False" se evalúa.
# Como resultado, la variable "not_logico" será True, ya que se niega el valor verdadero "False".

# Marc Delgado Ferreres