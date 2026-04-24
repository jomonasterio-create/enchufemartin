import tkinter as tk

# Función para actualizar la pantalla
def click_boton(valor):
    entrada.set(entrada.get() + str(valor))

# Función para limpiar pantalla
def limpiar():
    entrada.set("")

# Función para calcular resultado
def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.set(resultado)
    except:
        entrada.set("Error")

# Ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("300x400")

entrada = tk.StringVar()

# Pantalla
pantalla = tk.Entry(ventana, textvariable=entrada, font=("Arial", 20), bd=10, insertwidth=2, width=14, borderwidth=4)
pantalla.grid(row=0, column=0, columnspan=4)

# Botones
botones = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3)
]

for (texto, fila, col) in botones:
    if texto == '=':
        boton = tk.Button(ventana, text=texto, padx=20, pady=20, command=calcular)
    else:
        boton = tk.Button(ventana, text=texto, padx=20, pady=20, command=lambda t=texto: click_boton(t))
    boton.grid(row=fila, column=col)

# Botón limpiar
boton_clear = tk.Button(ventana, text="C", padx=20, pady=20, command=limpiar)
boton_clear.grid(row=5, column=0, columnspan=4, sticky="we")

ventana.mainloop()