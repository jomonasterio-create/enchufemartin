# obj enlatados 
peso=int(input("ingrese el peso del producto en gramos (numeros positivos); "))
while 0>=peso:
    print("el numero que elegiste es invalido")
    peso=int(input("ingrese nuevamente el numero: "))
sodio =int(input("ingrese la cantidad de sodio (en un rango de 1 a 100): "))
while sodio not in range(1,100):
    print("el numero que elegiste es invalido")
    sodio=int(input("ingrese nuevamente el numero: "))
pais=int(input("ingrese donde lo querra  1.-nacional/2.-internacional: "))
while pais<1 or pais>2:
    print("el numero que elegiste es invalido")
    pais=int(input("ingrese nuevamente el numero: "))


if peso<500:
    peso="-lata normal"
elif peso>501 and peso<1500:
    peso="-lata mediana"
elif peso>1501:
    peso="-lata grande"
elif peso<0:
    peso="-numero invalido"

if sodio<5:
    sodio="-lata normal"
elif sodio>5 and sodio<8:
    sodio="lata especial"
elif sodio>9:
    sodio="-lata acorazada"

if pais==1:
    pais="-lata nacional"
elif pais==2:
    pais="-lata internacional (con sticker sanitario)"

print(f"{peso}/{sodio}/{pais}")
