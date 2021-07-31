#Editor de texto para el reproductor
from tkinter.constants import PROJECTING
from pygame import mixer
from colorama import Back, Fore

#Inicio de reproduccion
    

def start(ruta):
    mixer.init()
    characters = "' "
    for x in range(len(characters)):
        ruta = ruta.replace(characters[x],"")

    ext = ruta.endswith(".ogg")
  
    if ext == False:
        print(ext)  
        ruta = ruta + ".ogg"
        print(ruta)
   
    
    mixer.music.load(ruta)
    mixer.music.set_volume(1)
    mixer.music.play()

#Herramientas

#Pause   
def pause():
    mixer.music.pause()  
#unpause
def unpause():
    mixer.music.unpause() 
#exit
def exit():
    mixer.music.stop()

        
        
    
        
        
        






