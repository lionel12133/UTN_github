vector_numero = [0] * 5

for i in range(5):
    vector_numero[i] = int(input(f"ingresa un numero {i+1}: "))

print(vector_numero)

vector_suma = [0] *10

for i in range(10):
    vector_suma[i] = int(input(f"ingresa un vector_suma {i+1}: "))

suma = 0

for x in range(10):
    suma += vector_suma[i]


print(suma)

vector_division = [0.0] *6

for k in range(6):
    vector_division[k] = int(input(f"ingresa un numero {k+1}: "))

division = 0

for k in range(6):
    division += vector_division[k]

promedio = division // 6

print(f"el promedio es de: {promedio}")

vector_mayor = [0] * 8

for i in range(8):
    vector_mayor[i] = int(input(f"ingresa un numero {i+1}: "))

contador = 0

for i in range(8):
    if vector_mayor[i] > 100:
        contador += 1
print(f"{contador} son los vec_numeros aquellos mayores a 100")



for i in range(10):
    vector_mayor[i] = int(input(f"ingresa un numero {i+1}: "))


vec_numeros = [0] * 7


for i in range(7):
    vec_numeros[i] = int(input(f"Ingrese el número {i+1}: "))


valor_maximo = vec_numeros[0]
posicion_maximo = 0

for i in range(7):
    if vec_numeros[i] > valor_maximo:
        valor_maximo = vec_numeros[i]
        posicion_maximo = i


print(f"El valor mas alto es {valor_maximo} y se encuentra en la posicion{posicion_maximo}.")

numeros = [0] * 6


for i in range(6):
    numeros[i] = int(input(f"Ingrese el numero {i+1}: "))


print("Array invertido:")
for i in range(5, -1, -1):
    print(numeros[i])

array1 = [0] * 5
array2 = [0] * 5


print("Cargar el primer array:")
for i in range(5):
    array1[i] = int(input(f"Elemento {i+1}: "))

print("Cargar el segundo array:")
for i in range(5):
    array2[i] = int(input(f"Elemento {i+1}: "))


iguales = True
for i in range(5):
    if array1[i] != array2[i]:
        iguales = False
        break


if iguales:
    print("Los arrays son iguales.")
else:
    print("Los arrays son diferentes.")


numeros = [0] * 10


for i in range(10):
    numeros[i] = int(input(f"Ingrese el numero {i+1}: "))


for i in range(10):
    if numeros[i] % 2 == 0:
        numeros[i] = 0


print("Array con pares reemplazados por cero:")
for i in range(10):
    print(numeros[i])

def buscar_primera_aparicion(array, valor):
    for i in range(len(array)):
        if array[i] == valor:
            return i
    return -1

numeros = [0] * 7
for i in range(7):
    numeros[i] = int(input(f"Ingrese el numero {i+1}: "))

buscar = int(input("Ingrese el valor a buscar: "))
posicion = buscar_primera_aparicion(numeros, buscar)

if posicion != -1:
    print(f"El valor se encuentra {posicion}.")
else:
    print("El valor no se encuentra en el array.")
