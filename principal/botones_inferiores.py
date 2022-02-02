from tkinter import *

class Boton(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        self.config(
        width=450,
        height=50,
        bg="#2c2b33"
        )
        
        # Texto que cambiará según la configuración
        self.operacion_variable = StringVar()

        # Partes del programa
        self.operacion_label = Label(self, textvariable=self.operacion_variable)
        self.iniciar_button = Button(self, text="Iniciar")
        self.imagen = PhotoImage(file="recursos/icono.png")
        self.configuraciones_button = Button(self, text="", image=self.imagen)
        self.observado = None

        # Configuracion de estilos de los objetos
        self.iniciar_button.config(
            fg="white",
            borderwidth=0,
            bg="cadetblue"
        )

        self.configuraciones_button.config(
            activebackground="#2c2b33", 
            bg="#2c2b33",
            borderwidth=0
        )

        # Posicionamiento de los objetos
        self.operacion_label.grid(row=0, column=0)
        self.iniciar_button.grid(row=0, column=1)
        self.configuraciones_button.grid(row=0, column=2)

        self.grid_propagate(False)
        self.grid_columnconfigure(1, weight=1)
    
    # Método para agregar al objeto al que observaremos para obtener los cambios de la configuración 
    def agregar_observador(self, observado):
        self.observado = observado
    
    # Método para actualizar la variable de texto de la operación
    def actualizar(self):
        self.operacion_variable.set(self.observado.obtener_modo_ordenamiento())