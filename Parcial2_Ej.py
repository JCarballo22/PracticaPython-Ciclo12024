
# Solicitar al usuario un número entero positivo N válido
validar = True
while validar:
    N = int(input("Ingrese un número entero positivo N: "))
    if N > 0:
        #break
        validar = False
    else:
        print("Por favor, ingrese un número entero positivo mayor que 0.")
# Calcular la suma de la serie
suma = 0
for i in range(1, N+1):
    suma += 1/i
# Mostrar el resultado
print(f"El resultado de la serie 1 + (1/2) + (1/3) + ... + (1/{N}) es: {suma}")

