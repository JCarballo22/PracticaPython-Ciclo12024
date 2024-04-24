#Ejemplo para break
print("While utilizando la sentencia break")
contador = 0

while contador < 10:
    contador += 1
    if contador == 7:
        break
    print("El actual del contador ", contador)
    
print("Valor del contador fuera del bucle: ",contador)
print("fin del programa, con sentencia break")


#Ejemplo sentencia continue
print("While con la sentecia continue")
cont = 0

while cont < 10:
    cont +=1

    if cont == 6:
        print("contador vale: ",cont)
        continue
        
    print("Valor actual de la variable: ",cont)

print("Fin del programa, Sentencia Continue")


#función len()

#Opción 1
print("Hola tiene ",len("hola")," Caracteres")

#Opción 2
texto = input("Escriba un texto: ")
longitud = len(texto)
print("La cadena de texto introducido tiene: ", longitud," caractectes")

