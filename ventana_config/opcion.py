from tkinter import *

class Opcion(Frame):
    def __init__(self, master, texto = "", lista_combobox = None):
        Frame.__init__(self, master)

        # Atributos de la clase
        self.texto = texto

        # Configuraciones del frame
        self.config(
            bg="#2c2b33",
            width=350,
            height=30
        )

        # Configuraciones de las partes del frame
        self.texto = Label(self, text=self.texto)

        # Configuracion de estilos de las partes del frame
        self.texto.config(
            fg="white",
            font=("ocean", 11),
            bg="#2c2b33"
        )

        # Posicionamiento de las partes del frame
        self.texto.grid(row=0, column=0)
        self.lista_combobox.grid(row=0, column=1)