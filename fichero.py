# Clase que se encarga de leer el fichero de configuración del Json y extraerá los datos
import json
from io import open

class Fichero:
    def __init__(self, ruta):
        self.ruta = ruta

    def modificar_json(self, clave_1, clave_2, informacion):
        # Abrimos el fichero y cargamos la información en formato json
        with open(self.ruta, "r") as fichero:
            self.cargar = json.loads(fichero.read())
        
        # Modificamos la información del Json
        self.cargar[clave_1][clave_2] = informacion

        # Guardamos la información nuevamente en el fichero Json
        with open(self.ruta, "w") as fichero:
            fichero.write(json.dumps(self.cargar, indent=4))
    
    def obtener_valor(self, clave_1, clave_2):
        # Abrimos el fichero y cargamos la información en formato json
        with open(self.ruta, "r") as fichero:
            self.cargar = json.loads(fichero.read())

        # Devolvemos la información solicitada
        return self.cargar[clave_1][clave_2]