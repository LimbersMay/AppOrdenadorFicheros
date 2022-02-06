from tkinter import *
from ventana_config.titulo import Titulo
from ventana_config.opcion import Opcion
from ventana_config.boton_guardar import BotonGuardar


class VentanaConfiguracion(Frame):
    def __init__(self, master, configuracion):
        Frame.__init__(self, master)

        # Atributos de la clase
        self.configuracion = configuracion

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

        # Obtenemos los objetos combobox de las opciones
        self.modo_combobox = self.modo_opcion.obtener_lista_opciones()
        self.algoritmo_combobox = self.algoritmo_opcion.obtener_lista_opciones()
        self.criterio_combobox = self.criterio_opcion.obtener_lista_opciones()

        # Le enviamos a los objetos opción la configuración actual del usuario
        self.modo_combobox.set(self.configuracion.obtener_modo_ordenamiento())
        self.algoritmo_combobox.set(self.configuracion.obtener_algoritmo())
        self.criterio_combobox.set(self.configuracion.obtener_criterio())

        # Le enviamos al objeto boton_guardar las listas de opciones (combobox)
        self.boton_guardar.enviar_lista_opciones(self.modo_combobox)
        self.boton_guardar.enviar_lista_opciones(self.algoritmo_combobox)
        self.boton_guardar.enviar_lista_opciones(self.criterio_combobox)
        
        self.boton_guardar.enviar_configuracion(self.configuracion)

        # Posicionamiento de los objetos
        self.titulo.grid(row=1, column=1)
        self.modo_opcion.grid(row=2, column=1)
        self.algoritmo_opcion.grid(row=3, column=1)
        self.criterio_opcion.grid(row=4, column=1)
        self.boton_guardar.grid(row=5, column=1)
    
    # Método para enviar el objeto de configuración
    def enviar_configuracion(self, configuracion):
        self.configuracion = configuracion