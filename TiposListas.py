print("Lista Vacia")
ListaVacia = []
print(ListaVacia)

print("\nListas Homogenias")

vocales = ["a","e","i","o","u"]
print(vocales)

numEnteros = [1,2,3,4,5]
print(numEnteros)

numDecimal = [1.5,2.2,3.3,4.9,5.1]
print(numDecimal)

valBool = [True,False,False,True,True]
print(valBool)


print("\nListas heterogenias")
nombre = "Yeseia"
apellido = "Rivera"
edad = 21
salario = 365.40
sexo = False

datos = ["Yeseia","Rivera",21,365.40,False]
datos2 = [nombre,apellido,edad,salario,sexo]

print(datos)
print(datos2)

print("Agregar un elemento a la lista")
letras = ["a","b","c","d"]
print(f"lista: {letras}")
letras.append("e")
letras.append("f")
print(f"lista: {letras}")

letras2 = ["b","d","f","g"]
letras2.insert(0,"a")
print(f"lista: {letras2}")
letras2.insert(2,"c")
print(f"lista: {letras2}")
letras2.insert(4,"e")
print(f"lista: {letras2}")


print(f"Lista: {vocales}")
vocales.pop()
print(f"Lista: {vocales}")
vocales.pop(2)
print(f"Lista: {vocales}")

vocales.remove("a")
print(f"Lista: {vocales}")
