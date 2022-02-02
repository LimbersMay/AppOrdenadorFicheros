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

    # Algoritmo de búsqueda binaria para encontrar la carpeta que más similitud tenga con el archivo
    def busqueda_binaria(self, arreglo_carpetas, valor):
        izquierda = 0
        derecho = len(arreglo_carpetas) - 1

        while izquierda <= derecho:
            medio = int((izquierda + derecho) / 2)

            # Si encuentro el valor que estoy buscando
            if self.determinar_similitud(valor, arreglo_carpetas[medio]) > 90:
                return medio

            elif arreglo_carpetas[medio] > valor:
                derecho = medio - 1

            else:
                izquierda = medio + 1

        return 0