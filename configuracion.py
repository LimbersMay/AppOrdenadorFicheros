# Clase observada por todas las demás clases que necesitan obtener la información del json de configuración
from fichero import *

class Configuracion:
    def __init__(self, ruta):
        self.fichero = Fichero(ruta)