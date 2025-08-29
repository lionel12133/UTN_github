# def saludar(nombre):
#     print(f"hola {nombre}")

# nombre = input("ingresa su nombre: ")
# saludar(nombre)

# num1 = int(input("ingrese un numero: "))
# num3 = int(input("ingrese otro numero: "))
    
# def operacion(num1, num3):
#     print(f"suma= {num1 + num3} resta= {num1 - num3} multiplicacion = {num1 * num3}")

# operacion(num1, num3)

# base = int(input("ingresa el base del triangulo: "))
# altura = int(input("ingresa el area del triangulo: "))

# def area_triangulo(base, altura):
#     print(f"el area del triangulo calculando su base y altura es: {base * altura//2}")

# area_triangulo(base, altura)

# def buscar_mayor(num1, num2, num3):
    
#     if num1 >= num2 and num1 >= num3:
#         if num2 >= num3:
#             return num1, num2, num3
#         else:
#             return num1, num3, num2
#     elif num2 >= num1 and num2 >= num3:
#         if num1 >= num3:
#             return num2, num1, num3
#         else:
#             return num2, num3, num1
#     else:
#         if num1 >= num2:
#             return num3, num1, num2
#         else:
#             return num3, num2, num1

# num1 = int(input("Introduce el primer número: "))
# num2 = int(input("Introduce el segundo número: "))
# num3 = int(input("Introduce el tercer número: "))


# numeros_ordenados = buscar_mayor(num1, num2, num3)
# print("Los números ordenados de mayor num1 menor son:", numeros_ordenados)

# numero = int(input("ingrese un numero: "))

# def  es_par(numero):
#     if numero == 0:
#         print("numero neutro")
#     elif numero % 2 == 0:
#         print(True)
#     else:
#         print(False)

# num_par_impar = es_par(numero)

# def convertir_minutos(minutos):
    
#     horas = minutos // 60  
#     minutos_restantes = minutos % 60  
    
#     return horas, minutos_restantes


# minutos = int(input("Introduce la cantidad de minutos: "))


# horas, minutos_restantes = convertir_minutos(minutos)
# print(f"{minutos} minutos son equivalentes a {horas} horas y {minutos_restantes} minutos.")

# edad = int(input("ingrese su edad: "))

# def verificar_acceso(edad):
#     if edad >= 18:
#         print(f"{True}, el usuario es mayor de edad")
#     else:
#         print(f"{False}, el usuario es menor de edad")

# edad_usuario = verificar_acceso(edad)

# anio_actual = 2025
# anio_nacimiento = int(input("ingresa su año de nacimiento: "))

# def calcular_edad(anio_nacimiento):
#     edad = anio_actual - anio_nacimiento
#     print(f"su edad de es: {edad}")

# calcular_edad(anio_nacimiento)








    