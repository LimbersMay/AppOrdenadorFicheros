# Clase que se encargará de ordenar todos los archivos que se encuentren en la ruta deseada a la ruta de destino

from configuracion import Configuracion
from manipulacionarchivo import ManipulacionArchivo
from fuzzywuzzy import fuzz
import os

class Ordenamiento:
    def __init__(self):
        
        # Atributos de la clase necesarios para realizar las operaciones
        self.configuracion = None
        self.manipulacion_archivo = ManipulacionArchivo()

    # Algoritmo que se encargará de ordenar todos los archivos
    def ordenar_recursos(self):
        pass

    def determinar_similitud(self, nombre_archivo, nombre_carpeta):
        return fuzz.token_set_ratio(nombre_archivo, nombre_carpeta)

    # Algoritmo que se encargará de buscar la carpeta con la que más similitud tenga con nuestro archivo
    def busqueda_lineal_arreglo(self, arreglo_carpetas, valor):
        similitudes = [self.determinar_similitud(carpeta, valor) for carpeta in arreglo_carpetas]
        
        return similitudes.index(max(similitudes))