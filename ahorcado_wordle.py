import random
import time

wordle = ["juego", "perro", "barco", "comer", "novio", "gotas", "gatos", "valor", "letra", "vidas", "sucio", "apego", "ansia", "agrio", "dulce", "aguda", "sabor"]
palabra_secreta = random.choice(wordle)
vidas = 6
lista_letras_adivinadas = []
print('_ ' * len(palabra_secreta))
print("Estoy pensando en una palabra de cinco letras.")
time.sleep(0.2)
while True:
    while True:
        time.sleep(0.2)
        letra_adivinada = input("Adivina una letra: ")
        if(len(letra_adivinada)!=1 and letra_adivinada.isnumeric()):
            vidas = vidas - 1
            print("Eso no es una letra intenta con una sola letra")
            print("Te quedan " + str(vidas) + " vidas")
        else:
            if letra_adivinada.lower() in lista_letras_adivinadas:
                vidas = vidas - 1
                print("Ya habias intentado con esa letra intenta con otra por favor")
                print("Te quedan " + str(vidas) + " vidas")
            else:
                lista_letras_adivinadas.append(letra_adivinada)
                if letra_adivinada.lower() in palabra_secreta:
                    print("Acertaste con la letra. Te queda poco!")
                    break
                else:
                    vidas = vidas - 1
                    print("Esa letra no esta en la palabra :(")
                    print("Te quedan " + str(vidas) + " vidas")
                    break

    if vidas == 0:
        print("Game Over :( \nLa palabra secreta era: "+ palabra_secreta + "\nJuega otra vez!")
        break

    estatus_actual = ""
 
    letras_faltantes = 0
    for letra in palabra_secreta:
        if letra in lista_letras_adivinadas:
            estatus_actual = estatus_actual + " " + letra
        else:
            estatus_actual = estatus_actual + " _ "
            letras_faltantes = letras_faltantes + 1
 
    print(estatus_actual)
    if letras_faltantes == 0:
        print("Felicidades la has adivinado y te ha(n) sobrado " + str(vidas) + " vida(s)!")
        print("La palabra secreta era: " + palabra_secreta + "\nJuega otra vez!")
        break