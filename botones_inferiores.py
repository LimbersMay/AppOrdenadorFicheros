from tkinter import *

class Boton(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        self.config(
        width=500,
        height=50,
        bg="#e7e6e1"
        )