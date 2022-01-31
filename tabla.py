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

        # Creamos la tabla
        self.tabla_scrollbar = Scrollbar(self)
        self.tabla_scrollbar.pack(side=RIGHT, fill=Y)

        self.tabla = Treeview(self, columns=("Carpeta", "Similitud"), yscrollcommand=self.tabla_scrollbar.set, selectmode="none")

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