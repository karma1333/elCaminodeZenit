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

    def significadoAmuleto(self,opcion):
        tip=open(f"archivos/tips/amuletos","r",encoding="UTF-8")
        contenido = tip.read()
        contenido2 = contenido.split("@")
        for dato in contenido2:
            leer = dato.split("#")
            #resultado = Articulos.amuletos(self)
            print(leer)
            if leer[0] == opcion:
                return leer[1]

    def libros(self):
        archivo = f"archivos/enlaces/enlacesLibros"
        articulo = []
        imagen = []
        url = []
        with open (archivo, encoding='utf=8') as libros:
            libro = libros.readlines()
            libros.close()
            for valor in libro:
                valor = valor.split(",")
                articulo.append(valor[0])
                imagen.append(valor[1])
                url.append(valor[2])
            return articulo,imagen,url

    def significadoLibro(self,opcion):
        tip=open(f"archivos/tips/libros","r",encoding="UTF-8")
        contenido = tip.read()
        contenido2 = contenido.split("@")
        for dato in contenido2:
            leer = dato.split("#")
            if leer[0] == opcion:
                return leer[1]

    def velas(self):
        archivo = f"archivos/enlaces/enlacesVelas"
        articulo = []
        imagen = []
        url = []
        with open (archivo, encoding='utf=8') as velas:
            vela = velas.readlines()
            velas.close()
            for valor in vela:
                valor = valor.split(",")
                articulo.append(valor[0])
                imagen.append(valor[1])
                url.append(valor[2])
            return articulo,imagen,url

    def significadoVela(self,opcion):
        tip=open(f"archivos/tips/velas","r",encoding="UTF-8")
        contenido = tip.read()
        contenido2 = contenido.split("@")
        for dato in contenido2:
            leer = dato.split("#")
            if leer[0] == opcion:
                return leer[1]







