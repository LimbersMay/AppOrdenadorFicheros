from tkinter import *
from tkinter.ttk import Treeview

class Tabla(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        
        self.config(
            width=480,
            height=150,
            bg="#e7e6e1"
        )

        # Asignamos el atributo de configuración que es el objeto al que observaremos
        self.configuracion = None

        # Creamos la tabla
        self.tabla_scrollbar = Scrollbar(self)
        self.tabla_scrollbar.pack(side=RIGHT, fill=Y)

        self.tabla = Treeview(self, columns=("Carpeta", "Similitud"), yscrollcommand=self.tabla_scrollbar.set, selectmode="browse")

        # Creamos las columnas
        self.tabla.column("#0", width=150, anchor=CENTER)
        self.tabla.column("Carpeta", width=150, anchor=CENTER)
        self.tabla.column("Similitud", width=150, anchor=CENTER)

        # Editamos los cabeceros
        self.tabla.heading("#0", text="Archivo")
        self.tabla.heading("Carpeta", text="Carpeta")
        self.tabla.heading("Similitud", text="Similitud")

        self.tabla.pack()

        # Configuramos el scrollbar
        self.tabla_scrollbar.config(
        command=self.tabla.yview
        )
    
    def agregar_observado(self, observado):
        self.configuracion = observado
    
    def actualizar(self):
        if hasattr(self.configuracion, "informacion"):
            self.informacion_filas = self.configuracion.obtener_informacion_ordenamiento()
        
            self.actualizar_tabla(self.informacion_filas)
    
    def actualizar_tabla(self, informacion_filas):
        self.tabla.delete(*self.tabla.get_children())

        for informacion_fila in informacion_filas:
            self.tabla.insert("", "end", text=informacion_fila[0], values=(informacion_fila[1], informacion_fila[2]))