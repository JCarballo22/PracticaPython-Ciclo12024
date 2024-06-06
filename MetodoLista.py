print("Lista vacia")

listaVacia = []
print(listaVacia)

print("Lista Homogenias")
String = ["hola","Como","estan"]
numEntero = [1,33,786,0,-9]
numDecimal = [2.36,7896.36,0.1,-55.55]
valBool = [True,False,False]
print(String,numEntero,numDecimal,valBool)

print("Lista Heterogenias")
datos = ["Castallo",23,1.86,False,-2,-2.2]
print(datos)

print("Agregar elementos a la lista")
letras = ["a","b","c","d"]
print(f"Lista: {letras}")
letras.append("e")
letras.append("f")
letras.append("g")
print(f"Lista: {letras}")

print("Lista original")
letras = ["b","d","f","g","a","a"]
print(f"lista: {letras}")
letras.insert(0,"a")
print(f"lista: {letras}")
letras.insert(2,"c")
letras.insert(4,"e")
print(f"lista: {letras}")


vocales = ["a","e","i","o","u"]
print(f"Lista: {vocales}")
vocales.pop()
print(f"Lista: {vocales}")

vocales.pop(2)
vocales.pop(0)
print(f"Lista: {vocales}")

vocales = ["a","e","i","o","u"]
print(f"Lista: {vocales}")
vocales.pop(-2)
print(f"Lista: {vocales}")

vocales.remove("e")
print(f"Lista: {vocales}")
vocales.remove("u")
vocales.remove("a")
print(f"Lista: {vocales}")

vocales = ["a","e","i","o","u"]
print(f"Lista: {vocales}")
del vocales[3]
print(f"Lista: {vocales}")

del vocales[0:2]
print(f"Lista: {vocales}")

vocales = ["a","e","i","o","u"]
print(f"Lista: {vocales}")
del vocales[:]
print(f"Lista: {vocales}")

vocales = ["a","e","i","o","u"]
print(f"Lista: {vocales}")
print(f"La letra o es en la posicion: {vocales.index("o")}")
posicionLetra = vocales.index("e")
print(f"La letra e es en la posicion: {posicionLetra}")
print(f"La letra u esta en el rango 2-final de la posición: {vocales.index("u",2)}")
print(f"La letra i esta en el rango 2-4 de la posición: {vocales.index("i",2,4)}")


invitados = ["Yesenia","David","Sara","Karla"]
amigos = ["Brandon","Marisol"]

print(f"Lista Invitados: {invitados} \nLista Amigos: {amigos}")
invitados.extend(amigos)
print(f"Lista Invitados: {invitados}")

numeros = [10,20]
print(f"Lista numeros: {numeros}")
numeros.extend(range(30,100,10))
print(f"Lista numeros: {numeros}")

print(f"Lista letras: {invitados}")
print(f"lista letras: {invitados.count("David")}")


invitados.reverse()
print(f"Lista letras: {invitados}")
print(f"Lista letras: {invitados}")
print(f"Lista letras: {invitados[0]}")
invitados.reverse()
print(f"Lista letras: {invitados[0]}")


numeros = [5,3,1,2,4]
vocales = ["o","u","e","a","i"]

print(f"Lista numero: {numeros}")
numeros.sort()
print(f"Lista numero: {numeros}")
numeros.sort(reverse=True)
print(f"Lista numero: {numeros}")

print(f"Lista vocales: {vocales}")
vocales.sort()
print(f"Lista vocales: {vocales}")
vocales.sort(reverse=True)
print(f"Lista vocales: {vocales}")


