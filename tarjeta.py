deuda=100000
print("su dinero es de $100.000 ten cuidado donde lo ocupas")
while True:
    try:
        print("--menu de su tarjeta--")
        print("1.-pago de tarjeta de credito")
        print("2.-simulacion de compras")
        print("3.-salir")
        selecc=int(input("haga su seleccion:  "))
        while selecc !=3:
            match selecc:
                case 1:
                    
                    try:
                        print("-ingrese un monto para realizar la compra de una tarjeta de credito-")
                        mont=int(input("monto: "))
                        if mont>=0 and mont<=100000:
                            print(f"su saldo actual es de {(deuda-mont)}")
                            break
                        else:
                            print("numero invalido")
                            break
                    except:
                        print("numero invalido")
        print("saliendo...") 
        break                      
                        
    except:
        print("numero invalido!!")