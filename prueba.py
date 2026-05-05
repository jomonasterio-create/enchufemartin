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
    print("-lata normal")
elif peso>501 and peso<1500:
    print("-lata mediana")
elif peso>1501:
    print("-lata grande")
elif peso<0:
    print("-numero invalido")

if sodio<5:
    print("-lata normal")
elif sodio>5 and sodio<8:
    print("-lata especial")
elif sodio>9:
    print("-lata acorazada")

if pais==1:
    print("-has elegido la lata nacional")
elif pais==2:
    print("-has elegido la lata internacional (con sticker sanitario)")

