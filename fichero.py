# Clase que se encarga de leer el fichero de configuración del Json y extraerá los datos
import json
from io import open

class Fichero:
    def __init__(self, ruta):
        self.ruta = ruta