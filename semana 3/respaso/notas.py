# realizar un programa que registre las notas de varios alumnos
# la cantidad de alumnos va a ser determinada por el usuario 
#cada alumno tendra cargada 3 notas
acumulacion_total_notas = 0

promedio_mayor = 0
alumno_mayor = 0
cantidad_alumnos = int(input("ingrese la cantidad de alumnos: "))
alumno = 1
while alumno <= cantidad_alumnos:
    total_notas = 0
    for examen in range (1, 4):
        nota = int(input("ingresar nota: "))
        total_notas += nota

    acumulacion_total_notas += nota
    promedio_alumno = total_notas / 3
    print(f"el alumno {alumno} tiene un promedio: {promedio_alumno}")

    if promedio_alumno > promedio_mayor:
        promedio_mayor = promedio_alumno
        alumno_mayor = alumno
    alumno += 1

promedio_general = acumulacion_total_notas // alumno

print(f"el promedio general del cursos es : {promedio_alumno}")
print(f"el promedio con mayor promedio es el numero: {alumno_mayor} con un promedio de {promedio_mayor}")