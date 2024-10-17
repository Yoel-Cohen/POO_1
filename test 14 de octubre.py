#Importar modulo
import tkinter as tk 

#Crear una ventana con nombre root
root = tk.Tk() 
#Agregar titulo
root.title("Window title")
#Agregar tamaño
root.geometry("500x300")

option=0

def change():
    #global 
    global option 
    if option==0:
        label.config(text="Text change")
        option=1
    elif option==1:
        label.config(text="This is my label")
        option=0

    #Config sirve para actualizar un label en tiempo real

# crear etiqueta
label=tk.Label(root, text="This is my label", font=("Arial", 18)) #Las clases con mayuscula
label.pack(padx=20, pady=20)

button=tk.Button(root, text="Cambio de boton",font=("Arial", 7), command=change )
button.pack(padx=7, pady=12)

#loop para que no se cierre la consola
root.mainloop()