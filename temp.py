temperaturas={
    "lunes":15,
    "martes":18,
    "miercoles":14,
    "jueves":9,
    "viernes":19
}
list=[]
for key, value in temperaturas.items():
    print(key, value)
    list.append(value)


list.sort()

print(f"la temperatura mas alta es el dia de {list[-1]} y la mas baja es {list[0]}")