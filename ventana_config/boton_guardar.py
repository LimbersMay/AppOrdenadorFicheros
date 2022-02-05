from tkinter import *

class BotonGuardar(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        # Atributos de la clase
        self.configuracion = None
        self.lista_opciones = []

        # Configuraciones del frame
        self.config(
            bg="#2c2b33",
            width=370,
            height=50
        )

        # Partes del programa
        self.boton = Button(self, text="Guardar", command=self.guardar_configuracion)
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
    
    # Enviamos los objetos combobox al frame
    def enviar_lista_opciones(self, lista_opciones):
        self.lista_opciones.append(lista_opciones)
    
    def guardar_configuracion(self):
        self.configuracion.modificar_modo_ordenamiento(self.lista_opciones[0].get())
        self.configuracion.modificar_algoritmo(self.lista_opciones[1].get())
        self.configuracion.modificar_criterio(self.lista_opciones[2].get())