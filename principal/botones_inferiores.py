from tkinter import *

class Boton(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        self.algoritmo_ordenamiento = None

        self.config(
        width=450,
        height=50,
        bg="#2c2b33"
        )
        
        # Texto que cambiará según la configuración
        self.operacion_variable = StringVar()

        # Partes del programa
        self.operacion_label = Label(self, textvariable=self.operacion_variable)
        self.iniciar_button = Button(self, text="Iniciar", command=self.iniciar)
        self.analizar_button = Button(self, text="Analizar")
        self.imagen = PhotoImage(file="recursos/icono.png")
        self.configuraciones_button = Button(self, text="", image=self.imagen)
        self.observado = None

        # Configuracion de estilos de los objetos
        self.iniciar_button.config(
            fg="white",
            borderwidth=0,
            bg="cadetblue"
        )

        self.analizar_button.config(
            fg="white",
            borderwidth=0,
            bg="darkred"
        )

        self.configuraciones_button.config(
            activebackground="#2c2b33", 
            bg="#2c2b33",
            borderwidth=0
        )

        # Posicionamiento de los objetos
        self.operacion_label.place(x=0, y=10)
        self.iniciar_button.place(x=190, y=10)
        self.analizar_button.place(x=230, y=10)
        self.configuraciones_button.place(x=400, y=2)

    # Método para agregar al objeto al que observaremos para obtener los cambios de la configuración 
    def agregar_observado(self, observado):
        self.observado = observado
    
    # Método para actualizar la variable de texto de la operación
    def actualizar(self):
        self.operacion_variable.set(self.observado.obtener_modo_ordenamiento())
    
    # Método que recibirá el objeto que contiene el algoritmo de ordenamiento
    def agregar_algoritmo(self, algoritmo):
        self.algoritmo_ordenamiento = algoritmo

    # Método que usará el método del objeto algoritmo para ordenar todos los archivos
    def iniciar(self):
        self.algoritmo_ordenamiento.ordenar_recursos()