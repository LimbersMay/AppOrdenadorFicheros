# Clase observada por todas las demás clases que necesitan obtener la información del json de configuración
from fichero import *

class Configuracion:
    def __init__(self, ruta):
        self.fichero = Fichero(ruta)
        self.observadores = []

    # Método para notificar a los observadores que un cambio ha ocurrido en la configuración 
    def notificar(self):
        for observador in self.observadores:
            observador.update()