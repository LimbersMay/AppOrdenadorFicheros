# Objeto observado por las demás clases para obtener las configuraciones del json

class Fichero:
    def __init__(self, observador):
        self.observador = observador
