from random import choice
def cartaTarot():
    """ Acceder a una baraja completa de Tarot
        y mostrar una carta de esa baraja"""
    numeros=["as","dos","tres","cuatro","cinco","seis","siete","ocho","nueve","diez","paje","caballo","reina","rey"]
    palos=["copas","espadas","oros","palos"]
    arcanos = ["arcanotrece","carro","colgado","diablo","elmundo","emperador","emperatriz","enamorado","ermitano",
               "estrella","fuerza","juicio","justicia","loco","luna","mago","papa","papisa","ruedafortuna","sol",
               "templanza","torre"]
    baraja=[]
    barajaArcanos = []
    barajaCompleta = []
    for numero in numeros:
        for palo in palos:
            baraja.append(f"{numero}de{palo}")

    for arcano in arcanos:
        barajaArcanos.append(arcano)

    for carta in baraja:
        barajaCompleta.append(carta)

    for arcano in barajaArcanos:
        barajaCompleta.append(arcano)

    unaCarta = choice(barajaCompleta)
    return unaCarta,baraja,barajaCompleta
def triada():
    """ Llamar a la función CartaTarot y mostrar tres cartas
        de la barajacompleta de Tarot"""
    cartas = cartaTarot()
    baraja = cartas[2]
    cartasUsadas = []
    numeroCartas = 0
    while numeroCartas < 3:
        carta = choice(baraja)
        if carta not in cartasUsadas:
            cartasUsadas.append(carta)
            numeroCartas += 1

    return cartasUsadas


class LecturaTarot:
    """ Leer las cartas del tarot """
    def __init__(self,carta):
        self.carta = carta

    def interpretacion(self):
        """ Mostrar por pantalla la definición
        de cada carta"""
        archivo = f"archivos/cartasTarot/cartas"
        # cartaSimple = cartaTarot()
        # leerCarta = cartaSimple[2]
        with open(archivo, encoding="utf-8") as leer:
            contenido = leer.read()
            contenido2 = contenido.split("@")

            for dato in contenido2:
                leer = dato.split("#")

                if self.carta == leer[0]:
                    separar = leer[0].split("de")
                    correcto = " de ".join(separar)
                    return correcto, leer[1]






