from tkinter import *

class Titulo(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        # Configuraciones
        self.config(
            bg="#2c2b33",
            width=500,
            height=50
        )