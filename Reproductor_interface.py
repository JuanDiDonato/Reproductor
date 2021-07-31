from tkinter import *
from tkinter import ttk
from tools import *


class Reproductor:

    

    def __init__(self, window):

        
        #Main window
        self.ventana = window
        self.ventana.title("Reproductor.ogg")
        
        #Container
        cont1 = LabelFrame(self.ventana)
        cont1.grid(row=0, column=0, columnspan=2, pady=10)

        #Search
        Label(cont1, text="Busca tu cancion").grid(row=1, column=1,)
        self.name = Entry(cont1)
        self.name.focus()
        self.name.grid(row=2, column=1, pady=10, columnspan=2)

        #Play
        self.play = ttk.Button(cont1, text="Play / Restart", command=self.inicio)
        self.play.grid(row=3, column=1, columnspan=2, pady=5)

        #Mensaje de salida
        self.message = Label(text="", fg="red")
        self.message.grid(row=4, column=1, columnspan=2, pady=5)

        #Pause
        self.play = ttk.Button(cont1, text="Pause", command=self.pausa)
        self.play.grid(row=5, column=1, columnspan=2, pady=5)

        #Unpause
        self.play = ttk.Button(cont1, text="UnPause", command=self.unpause)
        self.play.grid(row=6, column=1, columnspan=2, pady=5)


        #Volume
        #self.play = ttk.Button(cont1, text="+", command=self.volume)
        #self.play.grid(row=7, column=1, columnspan=2, pady=5)

        #Exit
        self.play = ttk.Button(cont1, text="Stop / Change", command=self.fin)
        self.play.grid(row=8, column=1, columnspan=2, pady=5)

    #Inicio
    def inicio(self):
        start(self.name.get())
        self.message["text"] = "Reproduciendo {} ".format(self.name.get())

    #Pausa
    def pausa(self):
        pause()
    #unpause
    def unpause(self):
        unpause()  
    #fin
    def fin(self):
        exit()
        self.name.delete(0, END)
        self.message["text"] = "Se a detenido la reproduccion."
   


if __name__ == "__main__":
    window = Tk()
    Reproductor(window)
    window.mainloop()
