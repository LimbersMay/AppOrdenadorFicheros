# Clase que se encargará de ordenar todos los archivos que se encuentren en la ruta deseada a la ruta de destino

import shutil
from fuzzywuzzy import fuzz
from walklevel import *

class Ordenamiento:
    def __init__(self):
        
        # Atributos de la clase necesarios para realizar las operaciones
        self.configuracion = None

    # Algoritmo que se encargará de ordenar todos los archivos
    def ordenar_recursos(self):

        # Enlistamos todas los archivos que se encuentren en la ruta de origen
        self.archivos = os.listdir(self.configuracion.obtener_ruta_origen())

        # Diccionario que contendrá los nombres de las carpetas con los que el archivo tuvo más similitud
        self.archivos_diccionario = dict((clave, []) for clave in self.archivos)

        bandera = True

        # Recorremos el árbol de directorios de la ruta de destino
        for directorio, carpetas, archivos in walklevel(self.configuracion.obtener_ruta_destino(), 1):
            for clave in self.archivos_diccionario:
                if not carpetas: # Si el directorio no tiene carpetas, pasamos al siguiente
                    continue
                
                # Comprobamos si la carpeta actual fue uno de los que más similitud tuvo con el archivo
                if os.path.basename(directorio) in self.archivos_diccionario[clave] or bandera:
                    self.archivos_diccionario[clave].append(self.busqueda_lineal_arreglo(carpetas, clave))
            bandera = False
        
        # Movemos los archivos a la ruta de destino
        for clave in self.archivos_diccionario:

            # Eliminamos el último elemento de la lista de coincidencias para que coincida con la profundidad
            self.archivos_diccionario[clave].pop()

            # Obtenemos la ruta de destino uniendo todas las carpetas con la que el archivo tuvo más similitud 
            ruta_destino = self.configuracion.obtener_ruta_destino() + "/" + "/".join(self.archivos_diccionario[clave]) + "/" + clave

            ruta_origen = self.configuracion.obtener_ruta_origen() + "/" + clave
            
            # Movemos o copiamos el archivo a la ruta de destino
            if self.configuracion.obtener_modo_ordenamiento().capitalize() == "Mover":
                shutil.move(ruta_origen, ruta_destino)
            
            elif self.configuracion.obtener_modo_ordenamiento().capitalize() == "Copiar":
                shutil.copy(ruta_origen, ruta_destino)           

    def agregar_configuracion(self, configuracion):
        self.configuracion = configuracion
            
    def determinar_similitud(self, nombre_archivo, nombre_carpeta):
        return fuzz.token_set_ratio(nombre_archivo, nombre_carpeta)

    # Algoritmo que se encargará de buscar la carpeta con la que más similitud tenga con nuestro archivo
    def busqueda_lineal_arreglo(self, arreglo_carpetas, valor):
        similitudes = [self.determinar_similitud(carpeta, valor) for carpeta in arreglo_carpetas]

        return arreglo_carpetas[similitudes.index(max(similitudes))]

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