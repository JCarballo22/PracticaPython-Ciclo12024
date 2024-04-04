#Operadores de Comparación
print("Introdusca  dos numero a comparar: \n")

numUno = int(input("Introdusca el primer numero: "))
numDos = int(input("Introdusca el segundo numero: "))

print("\n Los números a comparar son: ", numUno," y ", numDos, "\n")

if numUno == numDos:
    print("Los numeros son iguales...")
if numUno != numDos:
    print("Los numeros son diferentes...")
if numUno < numDos:
    print("Es Menor...")
if numUno > numDos:
    print("Es Mayor...")
if numUno <= numDos:
    print("Es Menor o Igual Que...")
if numUno >= numDos:
    print("Es Mayor o Igual Que...")


numTres = int(input("Introdusca un tercer numero: "))

#resultado = numUno < numDos
#print(numUno, "es < que ", numDos,": ",resultado)

resultado = numUno + numDos == numTres
print(numUno + numDos, "es < que ", numTres,": ",resultado)

