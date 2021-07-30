from colorama.ansi import Back
from Modulos.tools import tools, start, verification
from pygame import mixer
from colorama import Back, Fore

#inicio mixer de pygame
print(Back.CYAN + Fore.RED + "Reproductor .ogg --Programa en desarrollo")
print("Escriba el nombre de un archivo, o arrastrelo hasta la consola.")
print("El nombre del archivo NO DEBE tener espacios.")
mixer.init() 
string = str(input(Fore.RED + Back.CYAN + "Buscar Cancion: ")) #cancion = al dato str (string) que ingresa el usuario

#verificacion
verification(string)
#Inicio
start(string)
#herramientas
tools()










 



