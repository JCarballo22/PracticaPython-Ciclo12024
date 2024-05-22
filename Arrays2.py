

carros = ["Toyota","Mazda","Ford","Honda"]

print(carros)

print(carros[1])

x = carros[3] 
print(x)

#print(carros[4])

carros[2] = "Mercedez bens"

print(carros)

#carros[4] = "BMW"

print(carros)


c = len(carros)

print(c)

for i in carros:
    print(i)

print("fin")

carros.append("BMW")

print(carros)

carros.pop(2)

print(carros)