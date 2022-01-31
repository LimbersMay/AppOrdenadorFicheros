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