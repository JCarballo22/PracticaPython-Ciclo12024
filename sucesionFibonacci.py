#Ejercicio de Fibonacci
num1, num2 = 0,1
while num2 <= 5000:
    print(num1,num2, end=" ")
    num1 = num1 + num2
    num2 = num1 + num2

print("Fin.")

