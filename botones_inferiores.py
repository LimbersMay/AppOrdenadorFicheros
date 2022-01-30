from tkinter import *

class Boton(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        self.config(
        width=500,
        height=50,
        bg="#e7e6e1"
        )

        # Partes del programa
        self.operacion_label = Label(self, text="copiar")
        self.iniciar_button = Button(self, text="Iniciar")
        self.imagen = PhotoImage(file="recursos/icono.png")
        self.configuraciones_button = Button(self, text="", image=self.imagen)

        # Configuracion de estilos de los objetos
        self.iniciar_button.config(
            fg="white",
            borderwidth=0,
            bg="cadetblue"
        )

        self.configuraciones_button.config(
            activebackground="#2c2b33", 
            bg="#2c2b33",
            borderwidth=0
        )