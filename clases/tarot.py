import random
from random import choice

import streamlit
def cartaTarot():
    numeros=["as","dos","tres","cuatro","cinco","seis","siete","ocho","nueve","diez""paje","caballo","reina","rey"]
    palos=["copas","espadas","oros","palos"]
    arcanos = ["arcanotrece","carro","colgado","diablo","elmundo","emperador","emperatriz","enamorado","ermitano",
               "estrella","fuerza","juicio","justicia","loco","luna","mago","papa","papisa","ruedafortuna","sol",
               "templanza","torre"]
    baraja=[]
    for numero in numeros:
        for palo in palos:
            baraja.append(f"{numero} de {palo}")

    for arcano in arcanos:
        baraja.append(arcano)

    unaCarta = choice(baraja)
    return unaCarta, baraja

def triada():
    cartas = cartaTarot()
    baraja = cartas[1]
    cartasUsadas=[]
    numeroCartas=0
    while numeroCartas < 3:
        carta = choice(baraja)
        if carta not in cartasUsadas:
            cartasUsadas.append(carta)
            numeroCartas += 1
    return cartasUsadas


###tirada = cartaTarot()
###print(tirada[0])
###tres = triada()
###print(tres)