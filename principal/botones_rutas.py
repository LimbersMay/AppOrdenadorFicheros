from tkinter import *
from tkinter import filedialog

class BotonRuta(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        # Atributos de clase
        self.ruta_origen_variable = StringVar()
        self.ruta_destino_variable = StringVar()
        self.observado = None

        # Configuraciones
        self.config(
            bg="#2c2b33",
            width=500,
            height=50
        )

        self.grid_propagate(False)

        # Partes del programa
        # Textos de las rutas
        self.ruta_origen_label = Label(self, text="Ruta origen:")
        self.ruta_destino_label = Label(self, text="Ruta destino:")

        self.separador1 = Label(self, text="")
        self.separador2 = Label(self, text="")

        # Campos para introducir las rutas
        self.ruta_origen_entry = Entry(self, textvariable=self.ruta_origen_variable)
        self.ruta_destino_entry = Entry(self, textvariable=self.ruta_destino_variable)

        # Botones para seleccionar las rutas
        self.ruta_origen_button = Button(self, text="Seleccionar ruta", command=self.obtener_ruta_origen_ventana)
        self.ruta_destino_button = Button(self, text="Seleccionar ruta", command=self.obtener_ruta_destino_ventana)

        # Posicionamiento

        # Estilos a los objetos
        # ------------------------- Ruta origen ------------------------
        self.ruta_origen_label.config(
            fg="white",
            font=("ocean", 11),
            bg="#2c2b33"
        )

        self.ruta_origen_entry.config(
            width=45,
            bg="#e7e6e1",
            borderwidth=0
        )

        self.ruta_origen_button.config(
            fg="white",
            borderwidth=0,
            bg="cadetblue"
        )

        # ---------------- Ruta destino -----------------------
        self.ruta_destino_label.config(
            fg="white",
            font=("ocean", 11),
            bg="#2c2b33"
        )

        self.ruta_destino_entry.config(
            width=45,
            bg="#e7e6e1",
            borderwidth=0
        )

        self.ruta_destino_button.config(
            fg="white",
            borderwidth=0,
            bg="cadetblue"
        )

        # Separadores
        self.separador1.config(
            bg="#2c2b33"
        )
        self.separador2.config(
            bg="#2c2b33"
        )

        # Posicionamiento
        # Ruta origen
        self.ruta_origen_label.grid(row=1, column=0, sticky=W)
        self.ruta_origen_entry.grid(row=1, column=1)
        self.separador1.grid(row=1, column=2)
        self.ruta_origen_button.grid(row=1, column=3)

        # Ruta destino
        self.ruta_destino_label.grid(row=2, column=0, sticky=W)
        self.ruta_destino_entry.grid(row=2, column=1)
        self.separador2.grid(row=2, column=2)
        self.ruta_destino_button.grid(row=2, column=3)
    
    def agregar_observado(self, observado):
        self.observado = observado
    
    def actualizar(self):
        self.ruta_origen_variable.set(self.observado.obtener_ruta_origen())
        self.ruta_destino_variable.set(self.observado.obtener_ruta_destino())

    # Funciones para obtener la ruta de origen abriendo una ventana de dialogo de windows para seleccionar la carpeta
    def obtener_ruta_origen_ventana(self):
        archivo = filedialog.askdirectory(title="seleccionar ruta")
        self.observado.modificar_ruta_origen(archivo)
    
    def obtener_ruta_destino_ventana(self):
        archivo = filedialog.askdirectory(title="seleccionar ruta")
        self.observado.modificar_ruta_destino(archivo)