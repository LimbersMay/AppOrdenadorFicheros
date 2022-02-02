# Clase que se encargará de ordenar todos los archivos que se encuentren en la ruta deseada a la ruta de destino

from configuracion import Configuracion
from manipulacionarchivo import ManipulacionArchivo

class Ordenamiento:
    def __init__(self):
        
        # Atributos de la clase necesarios para realizar las operaciones
        self.configuracion = None
        self.manipulacion_archivo = ManipulacionArchivo()
