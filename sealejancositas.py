# print("seleccione numeros para sumar")
# asd=int(input("coloque un numero: "))

# dsa=int(input("coloque otro numero "))

# print(F"la suma de {asd} y {dsa} es:  {asd+dsa}")

# clave=input("ingrese su clave")
# if clave!="SHAZAM":
#    print("clave incorrecta")
# else:
#    print("clave correcta")


# name=input("cree su nombre de usuario de minimo 4 caracteres y max 10: ")
# if len(name)<4:
#    print("te faltan caracteres")
# elif len(name)>10:
#    print("te pasaste de caracteres")
# else:
#    print("nombre creado")

# pinn=(input("ingrese su pin: "))
# if len(str(pinn)) ==4:
#    print("entra")
# else:
#    print("no entra")

cand1=input("ingrese un candidato: ")
cand2=input("ingrese otro candidato: ")
v1=0
v2=0
votan=int(input("ingrese la cantidad de votantes: "))

for i in range(votan):
   voto=int(input(f"por quien votara?. 1.-{cand1} 2.-{cand2}"))
   if voto==1:
      v1+=1
   elif voto==2:
      v2+=1
   else:
      print("voto no valido")
if v1>v2:
   print(f"el ganador es {cand1} con {v1} votos") 
elif:
   print(f"el ganador es {cand2} con {v2} votos") 
else:
   print("empate")  