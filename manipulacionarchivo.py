import shutil

class ManipulacionArchivo:
    def __init__(self, ruta_origen = "", nombre_archivo = ""):
        # Configuraciones necesarias para realizar la operación del archivo
        self.ruta_origen = ruta_origen + "/"
        self.nombre_archivo = nombre_archivo
        self.ruta_destino = None