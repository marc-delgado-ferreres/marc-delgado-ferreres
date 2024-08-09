### Input ###

# Qué función tiene #

# La función "input()" se utiliza para recibir información ingresada por el usuario desde la consola y luego asignar esta información a variables.

# Ejemplo 1 #

# Podemos usar el "input()" para que el usuario ingrese una información y que no pase nada con esa información.

input("Por favor, no toques nada: ")

# En este ejemplo, se utiliza la función "input()" para solicitar al usuario que ingrese una información.
# El mensaje "Por favor, no toques nada: " se muestra en la consola para indicar al usuario que debe de ingresar alguna información.
# Después de que el usuario ingresa la información y presione el entro, no pasará nada, ya que esta información no se está asignando a ninguna variable.
# Como resultado, el programa continuará como si nada hubiera pasado.

# Ejemplo 2 #

# Podemos usar el "input()" para que el usuario ingrese una información y guardarla en una variable.

nombre_usuario = input("Ingrese su nombre: ")
print("Hola,", nombre_usuario, "!")

# En este ejemplo, se utiliza la función "input()" para solicitar al usuario que ingrese su nombre.
# El mensaje "Ingrese su nombre: " se muestra en la consola para indicar al usuario que debe de ingresar su nombre.
# Después de que el usuario ingresa su nombre y presiona enter, el valor ingresado se asigna a la variable "nombre".
# Luego, se utiliza la función "print()" para mostrar un mensaje que incluye el nombre ingresado por el usuario.
# Como resultado, se imprimirá un mensaje con el nombre proporcionado por el usuario.

# Ejemplo 3 #

# Podemos usar el "input()" para que el usuario ingrese una información y guardarla en una variable.
# Podemos observar en el ejemplo que se usa el "int()" para forzar a que la variable sea de tipo entero.

edad = int(input("Ingrese su edad: "))

print("Su edad es de", edad, "años")

# En este ejemplo, se utiliza la función "input()" para solicitar al usuario que ingrese su edad.
# El mensaje "Ingrese su edad: " se muestra en la consola para indicar al usuario que debe de ingresar su edad.
# Después de que el usuario ingresa su edad y presiona enter, el valor ingresado se convierte a un entero utilizando la función "int()".
# El valor entero resultante se asigna a la variable "edad".
# Luego, e utiliza la función "print()" para mostrar un mensaje que incluye la edad ingresada por el usuario.
# Como resultado, se imprimirá un mensaje con la edad proporcionada por el usuario.

# Marc Delgado Ferreres