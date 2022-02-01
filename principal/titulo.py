from tkinter import *

class Titulo(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        # Configuraciones
        self.config(
            bg="#2c2b33",
            width=500,
            height=50
        )

        # Partes del programa
        self.titulo = Label(self, text="Selección de rutas", font=("rockwell", 15), bg="#2c2b33", fg="white")
        self.titulo.grid(row=1, column=1)