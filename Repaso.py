#Formas de declarar variables
#Formas validas de declarar variables
mivariable = "Marisol"
mi_variable = "Marisol"
_mi_variable = "Brandon"
miVariable = "Brandon"
MIVARIABLE = "Brandon"
MiVariable = "Sara"
miVariable1 = "Sara"

#Formas no validas de declarar variables
#2miVariable = "sara"
#mi-Variable = "Sara"
#mi Variable = "Karla"

#Declaraciones de  variables 
miVar = "Raul"
miVar = 'Raúl'

#x = "verde"
#y = "azul"
#z = "amarrillo"

#x,y,z = 'verde','azul','amarrillo'

x=y=z = "Blanco"

print(x)
print(y)
print(z)

miVarX = 98
#miVarx = "noventa y ocho" 98
pesoCorporal = 75.5

print("El mensaje en pantalla")
print(999)
print(15.35)
print(miVariable)
print("Dame un numero: ", 9)
print("Tu Nombre es: " + mi_variable)
print("Tu nombre es:", miVariable1)
print("Tu numero es: " + str(miVarX))
print("Tu numero es:", miVarX)
print("El numero es: {0}, {1}".format(mivariable, MIVARIABLE))
print(f"El numero es: {mi_variable}")

palabras = input("Introduce un palabra ")
print(palabras)

numInt = int(input("Ingrese un numero entero "))
print("El numero ingresado es:", numInt)

numFloat = float(input("Ingrese un numero decimal "))
print(f"El numero decimal es: {numFloat}")

#peticion de un dato
nombre = input("¿Cual es su nombre?")
print("Hola "+ nombre +", Vamos arealizar una suma ")

numUno = int(input("Primer numero "))
numDos = int (input("Segundo numero "))

resultado = numUno + numDos

print(nombre, "El resultado de la suma es:", resultado)
