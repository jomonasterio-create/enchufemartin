op=0
total=0
while op!=4:
    print("1.- PC $500.000")
    print("2.- LGTV 55 pulgadas $450.000")
    print("3.- Microondas Mademsa $100.000")
    print("4.- Salir")
    print("Seleccione una opcion")
    try:
        op=int(input())
    except:
        print("seleccion incorrecta vuelva a intentar")    
    match op:
        case 1:
            print("El total a pagar es ",500000*1.19 )
            total+=500000*1.19
        case 2:
            print("El total a pagar es ",450000*1.19 )
            total+=450000*1.19
        case 3:
            print("El total a pagar es ",100000*1.19 )
            total+=100000*1.19
        case 4:
            print("Saliendo")
            print("El total a pagar es", total)
        case _:
            print("Opción inválida")