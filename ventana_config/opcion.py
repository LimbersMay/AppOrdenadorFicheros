from tkinter import *
from tkinter.ttk import Combobox

class Opcion(Frame):
    def __init__(self, master, texto = ""):
        Frame.__init__(self, master)

        # Atributos de la clase
        self.texto = texto
        self.lista_combobox = Combobox(self)

        # Configuraciones del frame
        self.config(
            bg="#2c2b33",
            width=280,
            height=20
        )

        # Configuraciones de las partes del frame
        self.texto = Label(self, text=self.texto)

        # Configuracion de estilos de las partes del frame
        self.texto.config(
            fg="white",
            font=("ocean", 11),
            bg="#2c2b33"
        )

        self.grid_propagate(False)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Posicionamiento de las partes del frame
        self.texto.grid(row=0, column=0, sticky=W)
        self.lista_combobox.grid(row=0, column=1, sticky=E)
    
    # Método para enviarle al objeto Combobox la lista de opciones
    def enviar_lista_opciones(self, lista_opciones):
        self.lista_combobox.config(values=lista_opciones)