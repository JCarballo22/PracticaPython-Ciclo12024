#Introducción de datos desde el teclado
#Cadenas o String

palabra = input("Introduce una palabra: ")
print(type(palabra))
print(f"El string que ingresas es: {palabra}")
print("El String ingresado es:", palabra)

#Enteros(int)
numInt = int(input("Ingresa un numero entero "))
print(type(numInt))
print(f"El numero ingresado entero es: {numInt}")

#Flotante (float)
numFloat = float(input("Ingresa un numero decimal "))
print(type(numFloat))
print("El numero ingresado decimal es: ",numFloat)

#Numeros Complejos (Complex)
numComplex = complex(input("Ingresa un numero "))
print(type(numComplex))
print("El numero ingresado complejo es: {0}".format(numComplex))


