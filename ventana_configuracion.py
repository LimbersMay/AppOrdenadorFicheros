from tkinter import *
from tkinter.ttk import Combobox
from ventana_config.titulo import Titulo
from ventana_config.opcion import Opcion
from ventana_config.boton_guardar import BotonGuardar

class VentanaConfiguracion(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        # Atributos de la clase
        self.configuracion = None

        # Configuraciones del master
        master.title("Configuraciones")
        master.geometry("370x150")
        master.config(bg="#2c2b33")

        # Configuraciones del frame
        self.config(bg="#2c2b33")

        # Partes del programa
        self.titulo = Titulo(self)
        self.modo_opcion = Opcion(self, "Tipo de operación: ")
        self.algoritmo_opcion = Opcion(self, "Algoritmo:")
        self.criterio_opcion = Opcion(self, "Criterio: ")

        self.boton_guardar = BotonGuardar(self)

        # Le enviamos a los objetos de opcion el listado de opciones
        self.modo_opcion.enviar_lista_opciones(["Copiar", "Mover"])
        self.algoritmo_opcion.enviar_lista_opciones(["Busqueda lineal", "Busqueda binaria"])
        self.criterio_opcion.enviar_lista_opciones(["Similitud", "Extension"])

        # Posicionamiento de los objetos
        self.titulo.grid(row=1, column=1)
        self.modo_opcion.grid(row=2, column=1)
        self.algoritmo_opcion.grid(row=3, column=1)
        self.criterio_opcion.grid(row=4, column=1)