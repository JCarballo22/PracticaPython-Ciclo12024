#Estructura condicional If Else
a = 20
b = 77

if b > a:
    print("B es mayor que A")
else:
    print("B es menor que A")


x = 4

if x > 5:
    print("X es mayor que 5")
else:
    print("X no es mayor que 5")


fruta = "Banana"
if fruta == "manzana":
    print("Es una Manzana")
else:
    print("No es una Manzana")

print("Sistema de notas")

nombre = input("Para comenzar, ingrese su nombre: ")

mate = float(input(nombre + " ¿Cual es tu nota en matematica?"))
ingles = float(input(nombre + " ¿Cual es tu nota en Ingles?"))
progra = float(input(nombre + " ¿Cual es tu nota de Fundamentos de programación?"))

promedio = (mate + ingles + progra)/3

if promedio >= 6:
    print(f"Felicidades {nombre} aprobastes con un promedio de: {round(promedio,2)}")
    print(f"Felicidades {nombre} aprobastes con un promedio de: {round(promedio,1)}")
else:
    print(f"Lo sentimos {nombre} reprobastes con un promedio de: {round(promedio,2)}")
    print(f"Lo sentimos {nombre} reprobastes con un promedio de: {round(promedio,1)}")

