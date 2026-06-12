# Crear un gestor de estacionamiento
# Un estacionamiento tiene cuatro pisos
# y cada piso tiene veinte espacios.
# Cuando entra un vehiculo preguntar qué tipo
# de vehiculo es (ligero 2000, mediano 3000, pesado 3500), luego acomodarlo en algun piso
# disponible. El menú debe tener las siguientes 
# alternativas.
vehiculos=[
    {"liviano":2000,},
    {"mediano":3000,},
    {"pesado":3500},
]
pisos=[
    {1:20,},
    {2:20,},
    {3:20,},
    {4:20},
]

ganancias=0
ingresados=0


def mostrar():
    c=1
    for key in vehiculos:
        print(f"{c}.-{key}")
        c+=1
    print("-"*38)
def mostrarpisos():
        c=1
        for key in pisos:
            print(f"{c}.-{key}")
            c+=1


while True:
    try:
        print(''' 
            ---GESTOR DE PARKING---
            1.- ingresar vehiculo
            2.- contar ganancias
            3.- contar vehiculos
            4.- salir''')
        op=int(input("ingrese una opcion: "))
        match op:
            case 1:
                while True:
                    print("---INGRESA LA CANTIDAD DE VEHICULOS---\n")
                    mostrar()
                    print("4.- salir")
                    clase=int(input("ingrese la clase que desea: "))
                    if pisos[0][1] == 20:
                    
                    if clase == 1:
                        ganancias+=2000
                        ingresados+=1
                    elif clase==2:
                        ganancias+=3000
                        ingresados+=1
                    elif clase==3:
                        ganancias+=3500
                        ingresados+=1
                    elif clase==4:
                        break
                    else:
                        print("seleccion incorrecta intente denuevo")
            case 2:
                print("---CONTAR GANANCIAS---\n")
                print(f"el total de ganancias es {ganancias} ")
            case 3:
                print("---CONTAR VEHICULOS---\n")
                print(f"el total de vehiculos es {ingresados}")
            case 4:
                print("SALIENDO...\n")
                break

            case _:
                print("OPCION INVALIDA INTENTE NUEVAMENTE..")
    except ValueError:
        print("valor invalido, intente denuevo")
print(pisos{0}{1})