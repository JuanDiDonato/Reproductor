from pygame import mixer

mixer.init() #inicia el reproductor
string = str(input("Buscar Cancion: ")) #cancion = al dato str (string) que ingresa el usuario
#Eliminacion de caracteres
characters = "' "
for x in range(len(characters)):
    string = string.replace(characters[x],"")




mixer.music.load(string)
mixer.music.set_volume(0.5)
mixer.music.play()


#Mientras
while True: 
    print("p para pausar")
    print("r para reanudar")
    print("c para cambiar")
    print("rr para reiniciar")
    print("s para salir")

    entrada = input("")
    if entrada == "p":
        mixer.music.pause()
    elif entrada == "r":
        mixer.music.unpause()
    elif entrada == "rr":
        mixer.music.rewind()    
    elif entrada == "s":
        mixer.music.stop()
        break
    elif entrada == "c":
        mixer.music.stop()
        string = str(input("Buscar Cancion: ")) #cancion = al dato str (string) que ingresa el usuario

        characters = "' "
        for x in range(len(characters)):
            string = string.replace(characters[x],"")
        mixer.music.load(string)
        mixer.music.set_volume(0.5)
        mixer.music.play()



 



