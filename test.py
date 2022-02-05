from tkinter import *
from ventana_configuracion import VentanaConfiguracion


def abrir_ventana_secundaria():
    root2 = Toplevel()
    ventana_secundaria = VentanaConfiguracion(root2)
    ventana_secundaria.pack()
    ventana_secundaria.mainloop()


root = Tk()
root.geometry("500x350")
root.config(bg="#2c2b33")

boton = Button(root, text="Click me!", command=abrir_ventana_secundaria)
boton.pack()

root.mainloop()