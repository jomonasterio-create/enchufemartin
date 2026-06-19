peliculas=[
    {"titulo": "Inception", "director": "Christopher Nolan",
     "genero": "Ciencia Ficcion", "anio": 2010, "rate": 8.9 },
    {"titulo": "Jurassic Park", "director": "Steven Spilberg",
     "genero": "Ciencia Ficcion", "anio": 1993 , "rate": 9.6},
    {"titulo": "Se7en", "director": "David Fincher",
     "genero": "Thiller", "anio": 1997 , "rate": 9.3},
]
# crear un gestor de peliculas
# EL titulo debe tener mas de 2 caracteres
# el año debe ser mayor a 1960 y debe der menor al año actual
# El director debe tener nombre y apellido
# mostar el sigueinte menú

while True:
    try:     
        print('''----PELICUILAS----
        1.- ingresar Pelicula
        2.- quitar Pelicula
        3.- Actualizar Pelicula
        4.- Mostar Peliculas
        5.- Mostrar solo los titulos
        6.- Mostrar los aos de las peliculas ordenados
        7.- Mostrar meplicula mejor calificada
        9.- Salir
        ''')
        op=int(input("seleccione una opcion: "))
        match op:
            case 1:
                
                print("--ingresa la pelicula--")
                titulo=input("ingresa el nombre de la plelicula: ")
                while len(titulo)==0 or len(titulo)<2:
                    titulo=input("nombre invalido, intente nuevamente: ")
                
                print("el director debe tener nombre y apellido")
                director=input("ingrese al director de pelicula: ")

            case 2:
                print("--Quite una plicula--")
                quitt=int(input("ingrese cual pelicula desea sacar: "))
            case 3:
                print("")
            case 4:
                for acc in peliculas:
    
                    print(f"titulo: {acc["titulo"]}\ndirector: {acc['director']}\ngenero: {acc['genero']}\naño: {acc['anio']}\nrating: {acc['rate']}\n{"-"*30}")
                
            case 5:
                print("")
            case 6:
                print("")
            case 7:
                print("")
            case 8:
                print("")
            case 9:
                print("")
    except ValueError:
        print("error intente nuevamente")
