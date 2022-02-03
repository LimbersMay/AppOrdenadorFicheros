# Clase que se encargará de ordenar todos los archivos que se encuentren en la ruta deseada a la ruta de destino

from manipulacionarchivo import ManipulacionArchivo
from fuzzywuzzy import fuzz
from walklevel import *

class Ordenamiento:
    def __init__(self):
        
        # Atributos de la clase necesarios para realizar las operaciones
        self.configuracion = None
        self.manipulacion_archivo = ManipulacionArchivo()

    # Algoritmo que se encargará de ordenar todos los archivos
    def ordenar_recursos(self):

        # Enlistamos todas los archivos que se encuentren en la ruta de origen
        self.archivos = os.listdir(self.configuracion.obtener_ruta_origen())

        # Diccionario que contendrá los nombres de las carpetas con los que el archivo tuvo más similitud
        self.archivos_diccionario = dict((clave, []) for clave in self.archivos)

        bandera = True

        # Recorremos el árbol de directorios de la ruta de destino
        for directorio, carpetas, archivos in walklevel(self.configuracion.obtener_ruta_destino(), 2):
            for clave in self.archivos_diccionario:
                if not carpetas: # Si el directorio no tiene carpetas, pasamos al siguiente
                    continue
                
                # Comprobamos si la carpeta actual fue uno de los que más similitud tuvo con el archivo
                if os.path.basename(directorio) in self.archivos_diccionario[clave] or bandera:
                    self.archivos_diccionario[clave].append(self.busqueda_lineal_arreglo(carpetas, clave))
            bandera = False
        
        # Movemos los archivos a la ruta de destino
        for clave in self.archivos_diccionario:
            # Obtenemos la ruta de destino uniendo todas las carpetas con la que el archivo tuvo más similitud 
            ruta_destino = self.configuracion.obtener_ruta_destino() + "/" + "/".join(self.archivos_diccionario[clave])

            ruta_origen = self.configuracion.obtener_ruta_origen()
            
            # Movemos el archivo a la ruta de destino
            self.manipulacion_archivo.set_nombre_archivo(clave)
            self.manipulacion_archivo.set_ruta_origen(ruta_origen)
            self.manipulacion_archivo.set_ruta_destino(ruta_destino)

            if self.configuracion.obtener_modo_ordenamiento() == "mover":
                self.manipulacion_archivo.mover_fichero()
            
            elif self.configuracion.obtener_modo_ordenamiento() == "copiar":
                self.manipulacion_archivo.copiar_fichero()
    
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