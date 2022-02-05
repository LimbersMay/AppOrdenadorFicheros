from tkinter import *

class Opcion(Frame):
    def __init__(self, master, texto = "", lista_combobox = None):
        Frame.__init__(self, master)

        # Atributos de la clase
        self.texto = texto
        self.lista_combobox = lista_combobox

        # Configuraciones del frame
        self.config(
            bg="white",
            width=350,
            height=30
        )
