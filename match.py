


# print("1.- opcion 1")
# print("2.- opcion 2")
# print("3.- opcion 3")
# op=int(input("seleccione una opcion: "))
# match op:
#     case 1:
#         print("selecciono la opcion 1")
#     case 2:
#         print("selecciono la opcion 1")
#     case 3:
#         print("selecciono la opcion 1")
#     case _:
#         print("opcion invalida ")



# op=0
# total=0
# while op!=4:
#     print("1.- xbox $350.000")
#     print("2.- ps5 $500.000")
#     print("3.- tele LG 60 pulgadas $600.000")
#     print("4.- salir")
#     op=int(input("seleccione una opcion: "))
#     match op:
#         case 1:
#             print("selecciono la opcion 1", 350000*1.19)
#             total+=350000*1.19
#         case 2:
#             print("selecciono la opcion 2", 500000*1.19)
#             total+=500000*1.19
#         case 3:
#             print("selecciono la opcion 3", 600000*1.19)
#             total+=600000*1.19
#         case 4:
#             print("saliendo ")
#             print(f"el total a pagar es {total}")
#         case _:
#             print("incorrecto")

def suma():
    num1=int(input("ingrese un numero:  "))
    num2=int(input("ingrese un segundo numero:  "))
    total=num1+num2
    print(f"su total de la suma de {num1} + {num2} es de {total}")
def resta():
    num1=int(input("ingrese un numero:  "))
    num2=int(input("ingrese un segundo numero:  "))
    total=num1-num2
    print(f"su total de la suma de {num1} - {num2} es de {total}")
def multi():
    num1=int(input("ingrese un numero:  "))
    num2=int(input("ingrese un segundo numero:  "))
    total=num1*num2
    print(f"su total de la suma de {num1} * {num2} es de {total}")
def div():
    num1=int(input("ingrese un numero:  "))
    num2=int(input("ingrese un segundo numero:  "))
    total=num1/num2
    print(f"su total de la suma de {num1} /  {num2} es de {total}") 
def salir():
    print("saliendo...")

total=0
op=0
while op!=5:
    print("--CALCULADORA--")
    print("1.-suma")
    print("2.-resta")
    print("3.-multiplicacion")
    print("4.-division")
    print("5.-salir")
    op=int(input("seleccione una operacion: "))
    match op:
        case 1:
            suma()
           
        case 2:
            resta()
        case 3:
            multi()
        case 4:
            div()
        case 5 :
            salir()
        case _:
            print("opcion invalida")
    



