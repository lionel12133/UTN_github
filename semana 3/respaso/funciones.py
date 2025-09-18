def pedir_turno():
    nombre = input("ingrese nombre: ")
    turno = input("ingrese turno (d/n): ")
    return nombre, turno
def registrar_turno(nombre, turno):
    if turno == "d" or turno == "n":
        return f"turno registrado: {nombre} trabajara en turno {turno}"
    else:
        return f"valor invalido"
    
def pedir_pago():
    horas = int(input("ingrese las horas trabjadas: "))
    turno = input("ingrese turno trabajado (d/n): ")
    return horas, turno

def calcular_pago(horas, turno):
    if turno == "d":
        return horas * 100
    elif turno == "n":
        return horas * 150
    else:
        return 0


def mensaje_agradecimiento():
    print("gracias por usar el sistema")