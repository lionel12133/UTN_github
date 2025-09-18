# for in range repaso



# numero = int(input("ingresa un numero: "))

# for i in range(-1, numero):
#     print(i + 1)

# numero = int(input("ingresa un numero: "))

# for i in range(1, 11):
#     resultado = numero * i
#     print(f"{numero} x {i} = {resultado}")

# acumulador = 0


# for i in range(1, 11):
#     num = int(input("ingrese su numero: "))
#     acumulador += num
#     if num == 0:
#         break

# print(f"la suma de todo los numeros es: {acumulador} y el promedio es {acumulador // i}")

# num1 = int(input("ingresa un numero: "))

# for i in range(1, 11):
#     resultao = num1 * i
#     print(f"los multiplos son {resultao}")}

# numero = int(input("ingrese un numero: "))

# for i in range(numero, 51):
#     if i % 2 == 1:
#         continue
#     print(i)

# Solicitar al usuario un número
n = int(input("Ingresa un número: "))

# Generar la pirámide
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()  # Nueva línea después de cada fila
