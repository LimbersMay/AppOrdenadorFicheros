from tkinter import *

class BotonGuardar(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        # Atributos de la clase
        self.configuracion = None

        # Configuraciones del frame
        self.config(
            bg="#2c2b33",
            width=370,
            height=50
        )

        # Partes del programa
        self.boton = Button(self, text="Guardar")
        self.separador = Label(self, text="")

        # Configuración de estilo del objeto
        self.boton.config(
            fg="white",
            borderwidth=0,
            bg="cadetblue"
        )

        self.separador.config(
            bg="#2c2b33"
        )

        # posicionamiento de los objetos
        self.boton.place(x=160, y=9)
    
    def enviar_configuracion(self, configuracion):
        self.configuracion = configuracion