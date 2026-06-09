productos={
    1:{"nombre": "maracuya","precio":2000},
    2:{"nombre": "pera", "precio": 1000},
    3:{"nombre": "sandia","precio": 3000},
}

def mostrarpr():
        print("-"*20)
        c=1
        for clave in productos:
            print(f"{c}.-{productos[clave]["nombre"]},{productos[clave]["precio"]}")
            c+=1
        print("-"*20)
def agregarprod():
    producagr = input("Ingrese el producto a ingresar: ")
    productos[list(productos.items())[-1][0]+1]=producagr
def eliminarpord():
    mostrarpr()
    elim = input("Seleccione el numero del producto a eliminar: ")
    productos.pop(elim-1)
def actualizarprod():
    mostrarpr()
    opc = int(input("Seleccione el numero del producto a actualizar: "))
    nuevaprr = input("Ingrese el nuevo producto: ")

    productos[opc-1] = nuevaprr







while True:
    print("-----FERIA-----")
    print("1.-agregar producto")
    print("2.-eliminar producto")
    print("3.-actualizar producto")
    print("4.-mostrar producto")
    print("5.-comprar productos")
    print("6.-crear boleta (calculo IVA) y salir")
    pou=int(input("seleccione una opcion: "))
    match pou:
        case 1:
              agregarprod()
        case 2:
              eliminarpord()
        case 3:
              actualizarprod()
        case 4:
              mostrarpr()
        case 5:
              print("")