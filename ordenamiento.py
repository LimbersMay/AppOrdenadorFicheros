# Clase que se encargará de ordenar todos los archivos que se encuentren en la ruta deseada a la ruta de destino

import shutil
from fuzzywuzzy import fuzz
from walklevel import *

class Ordenamiento:
    def __init__(self):
        
        # Atributos de la clase necesarios para realizar las operaciones
        self.configuracion = None

    # Algoritmo que se encargará de ordenar todos los archivos
    def ordenar_recursos(self, estado = 0, rutas_ignorar = []):

        # Enlistamos todas los archivos que se encuentren en la ruta de origen
        self.archivos = os.listdir(self.configuracion.obtener_ruta_origen())

        # Diccionario que contendrá los nombres de las carpetas con los que el archivo tuvo más similitud
        self.archivos_diccionario = dict((clave, []) for clave in self.archivos)

        # Obtenemos las rutas de origen y destino del objeto configuración para evitar acceder al fichero de configuración cada vez que se necesite
        self.ruta_origen = self.configuracion.obtener_ruta_origen()
        self.ruta_destino = self.configuracion.obtener_ruta_destino()

        bandera = True

        # Recorremos el árbol de directorios de la ruta de destino
        for directorio, carpetas, archivos in walklevel(self.ruta_destino, 1):
            for clave in self.archivos_diccionario:
                # Filtramos todos los elementos de las carpetas, agregamos todas son excepción de las carpetas temporales
                carpetas_filtradas = [carpeta for carpeta in carpetas if not carpeta.startswith('.')]

                # Comprobamos si la carpeta actual fue uno de los que más similitud tuvo con el archivo
                comprobante = os.path.basename(directorio) in self.archivos_diccionario[clave]

                if not carpetas_filtradas: # Si el directorio no tiene carpetas, pasamos al siguiente
                    if comprobante:
                        self.archivos_diccionario[clave].append(" ")
                    continue
                
                if comprobante or bandera:
                    self.archivos_diccionario[clave].append(self.busqueda_lineal_arreglo(carpetas_filtradas, clave))

            bandera = False
        
        # Movemos los archivos a la ruta de destino
        # estado = 0 -> El usuario desea que los archivos se ordenen
        # Estado = 1 -> El usuario desea que solo se analicen los directorios
        if estado == 0:
            for clave in self.archivos_diccionario:

                # Eliminamos el último elemento de la lista de coincidencias para que coincida con la profundidad
                self.archivos_diccionario[clave].pop()

                # Obtenemos la ruta de destino uniendo todas las carpetas con la que el archivo tuvo más similitud 
                ruta_destino = self.ruta_destino + "/" + "/".join(self.archivos_diccionario[clave]) + "/" + clave
                ruta_origen = self.ruta_origen + "/" + clave
                
                # Movemos o copiamos el archivo a la ruta de destino
                if self.configuracion.obtener_modo_ordenamiento().capitalize() == "Mover":
                    shutil.move(ruta_origen, ruta_destino)
                    
                
                elif self.configuracion.obtener_modo_ordenamiento().capitalize() == "Copiar":
                    shutil.copy(ruta_origen, ruta_destino)
        
        # Si el usuario desea que solo se analicen los directorios
        elif estado == 1:
            # Borramos todos los elementos finales de los arreglos
            for clave in self.archivos_diccionario:
                self.archivos_diccionario[clave].pop()
        
        # Generamos los datos que se mostrarán en la tabla de interfaz gráfica
        lista_informacion = [[] for _ in range(len(self.archivos))] # Lista que contendrá la información de cada archivo
        contador = 0
        for clave in self.archivos_diccionario:
            nombre_archivo = clave
            nombre_carpeta = self.archivos_diccionario[clave][-1]
            similitud = self.determinar_similitud(nombre_archivo, nombre_carpeta)

            lista_informacion[contador].append(nombre_archivo)
            lista_informacion[contador].append(nombre_carpeta)
            lista_informacion[contador].append(similitud)

            contador += 1
        
        self.configuracion.enviar_informacion_ordenamiento(lista_informacion)

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