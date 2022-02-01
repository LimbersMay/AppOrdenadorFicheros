# Clase observada por todas las demás clases que necesitan obtener la información del json de configuración
from fichero import *

class Configuracion:
    def __init__(self, ruta):
        self.fichero = Fichero(ruta)
        self.observadores = []

    # Método para notificar a los observadores que un cambio ha ocurrido en la configuración 
    def notificar(self):
        for observador in self.observadores:
            observador.actualizar()
    
    # Método para añadir un observador
    def agregar_observador(self, observador):
        self.observadores.append(observador)
    
    # Método para eliminar un observador
    def eliminar_observador(self, observador):
        self.observadores.remove(observador)

    # Método para obtener la ruta de origen
    def obtener_ruta_origen(self):
        return self.fichero.obtener_valor("directorios", "rutaOrigen")
    
    # Método para modificar la ruta de origen
    def modificar_ruta_origen(self, ruta):
        self.fichero.modificar_json("directorios", "rutaOrigen", ruta)