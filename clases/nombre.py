class NombreN:
    """ Obtener un número entre 0-9 dando un valor a cada letra de un texto """
    def __init__(self,nombre):
        self.nombre = nombre

    def valoresletras(self):
        conversor = {1:("a","á","j","s"),
                     2:("b","k","t"),
                     3:("c","l","u","u"),
                     4:("d","m","v"),
                     5:("e","é,","n","w"),
                     6:("f","o","ó","x"),
                     7:("g","p","y"),
                     8:("h","q","z"),
                     9:("i","í","r"),
                     10:("ñ"),
                     }

        lista =[]


        for n,lt in conversor.items():


            for letra in self.nombre.lower():
                if letra in lt:
                    lista.append(n)


        calculo = str(sum(lista))
        while len(calculo)>1:
            resultado = 0
            for n in calculo:
                resultado += int(n)
            calculo=str(resultado)
        return  calculo



# objeto1 = Nombre("Elle")
# print(objeto1.valoresletras())