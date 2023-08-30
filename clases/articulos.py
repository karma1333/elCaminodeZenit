from funciones.desplegable import opciones
class Articulos:
    """ mostrar unos articulos"""
    def __init__(self,opcionElegida):
        self.opcionElegida = opciones(opcionElegida)

    def amuletos(self):
        archivo = f"archivos/enlaces/enlacesAmuletos"
        articulo = []
        imagen = []
        url = []
        with open (archivo, encoding='utf=8') as amuletos:
            amuleto = amuletos.readlines()
            amuletos.close()
            for valor in amuleto:
                valor = valor.split(",")
                articulo.append(valor[0])
                imagen.append(valor[1])
                url.append(valor[2])
            return articulo,imagen,url

    def significadoAmuleto(self):
        with open(f"archivos/tips/amuletos") as tip:
            contenido = tip.read()
            contenido2 = contenido.split("@")
            for dato in contenido2:
                leer = dato.split("#")
                resultado = Articulos.amuletos(self)
                if leer[0] == resultado[0]:
                    return leer[1]










