total=0
precio=0
indie=0
estudio=0
e=0
md=0
M=0
tipo=0
while True:
    try:
        jueg=int(input("ingrese cuantos juegos quiere: "))
        if jueg>=5:
            print("cantidad de juegos invalida")
            break
        else:
            print("juegos fuera de rango")
    except:
        print("numero invalido")

while jueg != 0:
    while True:
        try:
            nombre=input("ingrese el nombre de su juego en MAYUSCULAS: ")
            if nombre==nombre.upper() and nombre==nombre.len():
                while True:
                    try:
                        precc=int(input("ingrese el precio que sea mayor a 20K: "))
                        if precc>0:
                            print("tu juego debe coinidir con el precio dicho")
                        elif precc>=20000 and precc<=40000:
                            tipo== "indie"
                            indie=+1
                        elif precc>=40000:
                            tipo== "estudio" 
                            estudio=+1
                        else:
                            print("invalido")    
                    except:
                        print("numero invalido")       
        except:
            print("nombre invalido")