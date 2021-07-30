#Editor de texto para el reproductor
from pygame import mixer
from colorama import Back, Fore

#Inicio de reproduccion
def start(ruta):
    characters = "' "
    for x in range(len(characters)):
        ruta = ruta.replace(characters[x],"")

    mixer.music.load(ruta)
    mixer.music.set_volume(0.75)
    mixer.music.play()

#Herramientas

def tools():
    #Mientras
    while True: 
        print("p para pausar")
        print("r para reanudar")
        print("c para cambiar")
        print("rr para reiniciar")
        print("s para salir")
        print("v para cambiar el volumen")

        entrada = input("")
        if entrada == "p":
            mixer.music.pause()
            print("PAUSADO")
        elif entrada == "r":
            mixer.music.unpause()
            print("PLAY")
        elif entrada == "rr":
            mixer.music.rewind()
            print("REINICIADO")  
        elif entrada == "v":
            vol = float(input("Valor entre 0 y 1: "))
            if vol < 0 or vol > 1:
                print(Back.RED + Fore.GREEN + "Valor invalido")
                print(Back.CYAN + Fore.RED +  "")
            else:    
                mixer.music.set_volume(vol)  
        elif entrada == "s":
            mixer.music.stop()
            print("Gracias por tu tiempo! --Programa en desarrollo")
            break
        elif entrada == "c":
            mixer.music.stop()
    
            string = str(input("Buscar Cancion: ")) 
            start(string)
            
   
#Comprobacion
def verification(ruta):
    if ruta == "":
        print(Back.RED + "Dato Invalido")
    
