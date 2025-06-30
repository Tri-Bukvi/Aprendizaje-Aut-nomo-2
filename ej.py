import random

def obtener_palabra_aleatoria():
    palabras=["gato", "computadora", "lampara", "parlante"]
    palabra_aleatoria=random.choice(palabras)
    return palabra_aleatoria
def mostrar_tabrero(palabra_secreta, letras_adivinadas):
    tablero=""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            tablero+=letra
        else:
            tablero+="[_]"
    print(tablero)

def jugar_ahorcado():
    palabra_secreta=obtener_palabra_aleatoria()
    letras_adivinadas=[]
    intentos_restantes=7

    while intentos_restantes>0:
        mostrar_tabrero(palabra_secreta, letras_adivinadas)
        letra=input("introduce una letra: ").lower()
        
        if letra in palabra_secreta:
            letras_adivinadas.append(letra)
            if set(letras_adivinadas)==set(palabra_secreta):
                print("Palabra adivinada")
                break
        else:
            intentos_restantes-=1
            print(f"letra incorrecta, te quedan {intentos_restantes}")
    if intentos_restantes==0:
        print(f"Perdiste, la palabra era {palabra_secreta}")

jugar_ahorcado()