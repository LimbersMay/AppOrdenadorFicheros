from tkinter import *
from ventana_principal import *

def main():

    root = Tk()
    ventana = Ventana(root)
    ventana.pack()
    ventana.mainloop()

main()