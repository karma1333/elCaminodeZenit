class Numerologia:
    """Calcular el numero personal según una fecha """
    def __init__(self,fecha):
        self.fecha = fecha



    def numeroPersonal(self):
        """ Devuelve  la suma de los digitos de la fecha de nacimiento,
            teniendo en cuenta numeros especiales, mostrando por pantanlla
            ese numero especial y haciendo la suma igual para reducir la fecha
            siempre a un digito (entre 1 y 9) """
        especiales = [11,13,15,16,19]
        digitos = []
        calculo = self.fecha.split("/")
        for numero in calculo:
            for digito in numero:
                digitos.append(int(digito))
        suma = sum(digitos)
        if suma not in especiales:
            while len(str(suma))>1:
                suma1 = int(suma / 10)
                suma2 = int(suma % 10)
                suma = suma1 + suma2
                if suma in especiales:
                    return suma
            return suma
        else:
            return suma



    def numero(self):
        """    Leer el contenido del archivo según el numero personal"""

        archivo = f"archivos/numerosPersonales/{Numerologia.numeroPersonal(self)}"

        with open(archivo, encoding="utf-8") as datos:
            contenido = datos.read()
            contenido2 = contenido.split("@")
        datos.close()
        return contenido2

    def numeroHistorico(self):
        """ Significado histórico de los números personales"""
        historico = Numerologia.numeroPersonal(self)
        if int(historico) <=9:
            archivo = f"archivos/numerosPersonales/{Numerologia.numeroPersonal(self)}mas"
        else:
            total = 0
            for di in str(historico):
                total += int(di)
            if total==19:
                total = 1
            archivo = f"archivos/numerosPersonales/{total}mas"

        with open(archivo, encoding="utf-8") as datos:
            contenido = datos.read()
            contenido2 = contenido.split("@")


        datos.close()
        return contenido2

    def zodiaco(self):
        """ cálculo según el dato fecha para mostrar
        los signos del zodiaco """
        fecha = self.fecha.split("/")
        comparador = []
        indice = 0
        if indice != 4:
            for f in fecha:
                indice += 1
                comparador.append(f)

        if comparador[1] == "01":
            if comparador[0] >= "19":
                signo = "acuario"
            else:
                signo = "capricornio"

        elif comparador[1] == "02":
            if comparador[0] >= "19":
                signo = "piscis"
            else:
                signo = "acuario"
        elif comparador[1] == "03":
            if comparador[0] >= "21":
                signo ="aries"
            else:
                signo = "piscis"
        elif comparador[1] == "04":
            if comparador[0] >= "21":
                signo = "tauro"
            else:
                signo = "Aries"
        elif comparador[1] == "05":
            if comparador[0] >= "21":
                signo = "geminis"
            else:
                signo = "tauro"
        elif comparador[1] == "06":
            if comparador[0] >= "21":
                signo = "cancer"
            else:
                signo = "geminis"
        elif comparador[1] == "07":
            if comparador[0] >= "23":
                signo = "leo"
            else:
                signo = "Cancer"
        elif comparador[1] == "08":
            if comparador[0] >= "23":
                signo = "Virgo"
            else:
                signo = "leo"
        elif comparador[1] == "09":
            if comparador[0] >= "23":
                signo = "Libra"
            else:
                signo = "virgo"
        elif comparador[1] == "10":
            if comparador[0] >= "23":
                signo = "Escorpio"
            else:
                signo = "Libra"
        elif comparador[1] == "11":
            if comparador[0] >= "22":
                signo = "Sagitario"
            else:
                signo = "Escorpio"
        elif comparador[1] == "12":
            if comparador[0] >= "22":
                signo = "capricornio"
            else:
                signo = "Sagitario"

        archivo = f"archivos/zodiaco/{signo.lower()}"

        with open(archivo, encoding='utf-8') as z:
            contenido = z.read()
            contenido2 = contenido.split("#")
            z.close()

            return contenido2










