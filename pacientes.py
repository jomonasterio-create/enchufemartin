# Crear el gestor de pacientes en un centro medico
# Para poner el nombre se debe validar que no esté vacio
# y además tenga mas de 8 caracteres
# Para la prevision de salud solo existen 3 posibles valores
# Fonasa, Isapre o Fodesa
# Al ingresar un paciente, se debe poner la temperatura
# Crear una funcion que valide si está grave o no 
# Para que esté grave debe tener más de 39°



pacientes=[
    {"nombre": "aquiles baeza", "prevision": "fonasa", "temperatura":34.6, "grave": False}
]

def temp(temperatura):
        if temperatura< 39:
            return False
        elif temperatura> 39:
            return True



        




while True:
    try:
        print('''---Gestor de pacientes---
1.- ingresa al paciente
2.- ver al paciente
3.- salir''')
        op=int(input("ingresa una opcion: "))
        dicc={}
        match op:
            case 1:
                print("--ingresa al paciente--")
                nombre=input("ingresa el nombre del paciente: ")
                while len(nombre)==0 or len(nombre)>8:
                    nombre=input("nombre invalido, intente nuevamente: ")
                    
                previocion=int(input("----ingresa su previcion-----\n1.-fonasa\n2.-isapre\n3.-fodesa\nseleccione una opcion: "))
                while previocion not in [1,2,3]:
                    previocion=int(input("ingresa su previcion nuevamente\n1.-fonasa\n2.-isapre\n3.-fodesa"))
                
                temperatura=float(input("ingresa la temperatura del paciente: "))
                
            case 2:
                
                print(f"{pelic}")


                for i in dicc:
                    pacientes.append(dicc)
                print(pacientes)
            case 3:
                print("saliendo...")
                break
    except ValueError:
        print("invalido")
    

