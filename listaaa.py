# num=[12,43,34,16,87,54,98]

# num.sort()
# men=num[0]
# may=num[-1]
# print(f"el numero mayor es {may} y el numero menor es {men}")
# print(f"{num}")
# num.reverse()
# print(f"{num}")

#-----------------------------------------------------------------------------


# prec=[
#     ["pera", 1290],
#     ["papas", 10000],
#     ["zanahoria", 2340],
#     ["repollo", 5790]
# ]
# prectotal=0
# for produc in prec:
#     prectotal+=produc[1]



# print(f"la suma de todos los numeros es de {prectotal}")
notas={4.6,6.9,4.1}

def agregarnotas():
    notass=float(input("ingresa la nota: "))
    notas.append(notas)
    notasingre.append(notas)
    cantinotas+=1

def mostrarnotas():
    print("-"*20)
    c = 1
    for f in notas:
        print(f"{c}.- {f}")
        c += 1
    print("-"*20)

while True:
    try:
        print(''' 
        1.- agrega notas a la lista creada
        2.- muestre por pantalla todas las notas ingresadas 
        3.- muestra la cantidad de notas ingresadas 
        4.- optenga el promedio de las notas
        5.- SALIR   ''')
        op=int(input("seleccione una opcion: "))
        notasingre=[]
        cantinotas=0
    except ValueError as e:
        print("error", e)
        match op:
            case 1:
                agregarnotas()
            case 2:
                mostrarnotas()
            case 3:
                print(f"las notas son {len(notas)}")
            case 4:
               for n in notas:
                   suma=suma+n
                   prom=suma/len(notas)
                   print(f"el promedio es {round(prom, 1)}")
