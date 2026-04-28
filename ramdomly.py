# import random
# num=random.randint(1,19)
# print(num)

# for i in range(num):
#     print("hola vicente")

# for i in range(10):
#     print(f"{num}x{i}={num*i}")


# import random 
# tiros=random.randint(60,190)
# tiros2=random.randint(60,190)
# tiros3=random.randint(60,190)


# for i in range(1):
#  print ("tiro 1:su tiro fue de potencia de",tiros ,"metros")
#  print ("tiro 2:su tiro fue de potencia de",tiros2 ,"metros")
#  print ("tiro 3:su tiro fue de potencia de",tiros3 ,"metros")
# if tiros>tiros2:
#     print(f"el tiro 1 fue mas potente con {tiros} metros")
# elif tiros2>tiros3:
#     print(f"el tiro 2 fue mas potente con {tiros2} metros")  
# elif tiros3>tiros:
#     print(f"el tiro 3 fue mas potente con {tiros3} metros")      
# else:
#    print("los jugadores empataron")   
# 
# 
# 

# import random
# turno=0
# total=0
# while total<=50:
#    lanzar=(input("lanze el dado con la tecla [f]:  "))
#    if lanzar=="f":
#       dado=random.randint(1,6)
#       dado1=random.randint(1,6)
#       print(f"su dado1 a sacado {dado}")
#       print(f"su dado2 a sacado {dado1}")
#       total+=dado+dado1
#       print(f"el lugar del tablero en le que estas es: {total}")
#       turno+=1
#       print(f"los turnos que te tomaron llegar son {turno}")
import random
ran=random.randint(1,100)
i=0
while i<5:
    num=int(input("adivina el numero: "))
    if num<ran:
        print("te falta")
        i+=1
    elif num>ran:
        print("te pasaste")
        i+=1
    elif num==ran:
        print("le acertaste!!!")
        i+=1
print(f"se acabaron tus intentos el numero era {ran}")


    

