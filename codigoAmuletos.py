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






