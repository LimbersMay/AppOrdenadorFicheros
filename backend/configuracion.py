# Clase observada por todas las demás clases que necesitan obtener la información del json de configuración
from backend.fichero import Fichero

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

        # Notificamos a los observadores que ha habido un cambio en la configuración
        self.notificar()
    
    # Método para obtener la ruta de destino
    def obtener_ruta_destino(self):
        return self.fichero.obtener_valor("directorios", "rutaDestino")
    
    # Método para modificar la ruta de destino
    def modificar_ruta_destino(self, ruta):
        self.fichero.modificar_json("directorios", "rutaDestino", ruta)

        # Notificamos a los observadores que ha habido un cambio en la configuración
        self.notificar()
    
    # Método para obtener el modo de ordenamiento
    def obtener_modo_ordenamiento(self):
        return self.fichero.obtener_valor("ordenamiento", "operacion")
    
    # Método para modificar el modo de ordenamiento
    def modificar_modo_ordenamiento(self, modo):
        self.fichero.modificar_json("ordenamiento", "operacion", modo)

        # Notificamos a los observadores que ha habido un cambio en la configuración
        self.notificar()
    
    # Método que recibirá la información que la tabla necesita (archivo, carpeta, similitud)
    def enviar_informacion_ordenamiento(self, arreglo_tuplas):
        self.informacion = arreglo_tuplas

        self.notificar()
    
    # Método para obtener la información que la tabla necesita
    def obtener_informacion_ordenamiento(self):
        return self.informacion