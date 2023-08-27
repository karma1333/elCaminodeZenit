class Numerologia:
    """Calcular el numero personal según una fecha """
    def __init__(self,fecha):
        self.fecha = fecha



    def numeroPersonal(self):
        """ Devuelve un numero entre 1 y 9"""
        suma = 0
        calculo = self.fecha.split("/")
        for numero in calculo:
            for digito in numero:
                suma += int(digito)

        suma1 = int(suma / 10)
        suma2 = int(suma % 10)
        fin = suma1 + suma2
        return fin

    def numero(self):
        """ Significado de los números personales"""

        archivo = f"archivos/numerosPersonales/{Numerologia.numeroPersonal(self)}"

        with open(archivo, encoding="utf-8") as datos:
            contenido = datos.read()
            contenido2 = contenido.split("@")
        datos.close()
        presentacion = contenido2[0]
        definicion = contenido2[1]
        return presentacion,definicion

    def numeroHistorico(self):
        """ Significado histórico de los números personales"""

        archivo = f"archivos/numerosPersonales/{Numerologia.numeroPersonal(self)}mas"

        with open(archivo, encoding="utf-8") as datos:
            contenido = datos.read()

        datos.close()
        return contenido

    def zodiaco(self):
        fecha = self.fecha.split("/")
        dia = fecha[0]
        mes = fecha[1]
        lista = []
        signos = ["","capricornio","acuario", "piscis", "aries", "tauro", "geminis", "Cáncer",
                  "leo", "virgo", "libra", "escorpio", "sagitario"]
        for m in range(1, 13):
            if m == int(mes):
                if int(dia) <= 21:
                    lista.append(signos[m])

                else:
                    indice = m +1
                    lista.append(signos[indice])
        print(lista)
        archivo = f"archivos/zodiaco/{lista[0]}"
        with open(archivo, encoding='utf-8') as z:
            contenido = z.read()
            return contenido


#ana = Numerologia("10/06/1977")
#numeroP = ana.zodiaco()
#print(numeroP)








