def calcular_serie(N):
    """
    Calcula la suma de la serie 1 + (1/2) + (1/3) + ... + (1/N).
    
    Parámetros:
    N (int): Un número entero positivo.
    
    Retorna:
    float: El resultado de la serie.
    """
    suma = 0
    for i in range(1, N+1):
        suma += 1/i
    return suma

# Solicitar al usuario un número entero positivo N válido
while True:
    try:
        N = int(input("Ingrese un número entero positivo N: "))
        if N > 0:
            break
        else:
            print("Por favor, ingrese un número entero positivo mayor que 0.")
    except ValueError:
        print("Por favor, ingrese un número entero positivo válido.")

# Calcular y mostrar el resultado
resultado = calcular_serie(N)
print(f"El resultado de la serie 1 + (1/2) + (1/3) + ... + (1/{N}) es: {resultado}")