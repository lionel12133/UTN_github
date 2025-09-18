import funciones as fn
# from funciones import * (otra maner de importar)
while True:
    print("----menu principal----")
    print("1. registrar turno")
    print("2. calcular pago")
    print("3. mostrar mensaje de agradecimiento")
    print("4. salir")

    opcion = input("ingrese opcion: ")
    if opcion == "1":
        no, tu = fn.pedir_turno()
        print(fn.registrar_turno(no, tu))
    elif opcion == "2":
        hs, tu = fn.pedir_pago()
        print(fn.calcular_pago(hs, tu))
    elif opcion == "3":
        fn.mensaje_agradecimiento()
    elif opcion == "4":
        break
    else:
        print("opcion invalida, ingresar de nuevo: ")
