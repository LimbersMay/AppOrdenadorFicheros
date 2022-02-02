import shutil

class ManipulacionArchivo:
    def __init__(self, ruta_origen = "", nombre_archivo = ""):
        # Configuraciones necesarias para realizar la operación del archivo
        self.ruta_origen = ruta_origen + "/"
        self.nombre_archivo = nombre_archivo
        self.ruta_destino = None

    # Métodos necesarios de la clase
    def mover_fichero(self):
        try:
            shutil.move(self.ruta_origen + self.nombre_archivo, self.ruta_destino + self.nombre_archivo)
        except:
            return

    def copiar_fichero(self):
        shutil.copy(self.ruta_origen + self.nombre_archivo, self.ruta_destino + self.nombre_archivo)