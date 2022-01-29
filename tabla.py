from tkinter import *

class Tabla(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        
        self.config(
            width=480,
            height=150,
            bg="#e7e6e1"
        )