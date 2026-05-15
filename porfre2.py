

try:
    notas=int(input("Ingrese la cant de notas: "))
    suma=0
except:
    print("coloque solamente numeroes enteros")
for i in range(notas):
    while True:
        try:
            n=float(input(f"Ingrese la nota {i+1}: "))
            if 1<=n<=7:
                suma=suma+n
                break
            else:
                print("nota fuera de rango (1.0 a 7.0)")
            
        except:
            print("nota incorrecta intende denuevo ")


prom=suma/notas
print("El promedio es",round(prom,1) )
if prom>=4:
    print("Alumno aprobado")
else:
    print("Alumno reprobado")