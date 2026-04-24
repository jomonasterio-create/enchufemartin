opa=0
while opa!=4:
    print("1.-calculadora")
    print("2.-votatoon")
    print("3.-tienda")
    print("4.-salir")
    match opa:
        case 1:
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
        case 2:
             
                
        case 3:
                        
        case 4:
                        
        case _:
