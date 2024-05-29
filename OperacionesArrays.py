from numpy import*

a = array([64,55,21,11,19,9])
b = array([12,-9,0,22,-9,64])

#Sumar los dos arreglos elemento a elemento
sumA = a + b
print(a)
print(b)
print(sumA)

#Resta los elementos a elemento
resA = a - b
print(a)
print(b)
print(resA)

#Multiplicación elemento a elemento
mulA = a * b
print(mulA)


#Multiplicacion por 0.2/4.36 todos los elementos
varmul = 0.2 * a
print(a)
print(varmul)

varSum = a + 7
print(varSum)

varRes = a - 9
print(varRes)

#Operaciones relacionales de arreglos
x = array([5.1,2.4,3.8,3.9])
y = array([4.2,8.7,3.9,0.3])
z = array([5,2,4,4])+ array([1,4,-2,-1])/10.0

print(x)
print(y)
print(x<y)

print(x==z)

print(any(x<y))
print(any(x==z))

print(all(x==z))

#Operaciones matemáticas de Numpy con matrices
e = [[2,3],[4,5]]
f = [[5,2],[1,4]]

#Concatenando lista
print(e+f)

#Conversión de matriz a arreglo
e = array(e)
f = array(f)


#suma y restra de matrices
print(e+f)
print(e-f)

#multiplicación elemento a elemento
print(e*f)

#multiplicacion de matrices
print(dot(e,f))


#funciones especiales
h = array([[4,2,5],[2,8,4],[6,9,5]])
print(h)

#suma de los elementos de la matriz
print(sum(h))

#producto de todos los elemtos
print(prod(h))

