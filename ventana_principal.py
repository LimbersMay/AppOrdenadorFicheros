from tkinter import *
from configuracion import Configuracion
from ordenamiento import Ordenamiento

from principal.botones_inferiores import Boton
from principal.campos_rutas import CampoRuta
from principal.tabla import Tabla
from principal.titulo import Titulo

class Ventana(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        
        # Configuración básica
        master.title("Organizador de archivos")
        master.geometry("500x350")
        master.config(bg="#2c2b33")

        self.config(bg="#2c2b33")

        # Objeto al que observaremos para obtener los cambios de la configuración
        self.configuracion = Configuracion('json/configuracion.json')
        self.ordenamiento = Ordenamiento()

        # Partes del programa
        self.titulo = Titulo(self)
        self.campos_rutas = CampoRuta(self)
        self.tabla = Tabla(self)
        self.botones = Boton(self)

        # Enviamos el objeto al que observaremos para obtener los cambios de la configuración
        self.botones.agregar_observado(self.configuracion)
        self.botones.agregar_algoritmo(self.ordenamiento)
        self.campos_rutas.agregar_observado(self.configuracion)

        # Le indicamos al objeto observado quiénes son sus observadores
        self.configuracion.agregar_observador(self.botones)
        self.configuracion.agregar_observador(self.campos_rutas)

        # Le mandamos al objeto ordenamiento el objeto que contiene todas las configuraciones
        self.ordenamiento.agregar_configuracion(self.configuracion)

        # Notificamos a todos los observadores cúales son las configuraciones actuales
        self.configuracion.notificar()

        # Posicionamiento
        self.titulo.grid(row=1, column=1)
        self.campos_rutas.grid(row=2, column=1)
        self.tabla.grid(row=3, column=1)
        self.botones.grid(row=4, column=1)
        