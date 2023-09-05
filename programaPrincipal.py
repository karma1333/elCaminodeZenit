""" Programa con salida gráfica a traves de streamlit que
    solicita datos al usuario y  muestra contenido que está almacenado
    en archivos.
    En el menú principal hay varias opciones que derivan  en otras opciones.

    Programa creado por Ana María Caballero Rodríguez
"""


from clases.numerologia import *
from clases.nombre import *
import datetime
import streamlit as st
from PIL import Image
from clases.articulos import *
from clases.leerTarot import *

st.set_page_config(
    page_title="El camino del Zenit",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        'Get Help': 'mailto:antakarana3@gmail.com',
        'Report a bug': "mailto:antakarana3@gmail.com",
        'About': " El camino del *Zenit* "}
                )




## DESPLEGABLE DE LA DERECHA
with st.sidebar:

    st.write("Escribe tu nombre y tu selecciona tu fecha de nacimiento en el calendario")
    nombre = st.text_input(" ¿Como te llamas?")
    fechaDeNacimiento = st.date_input("¿Cúal es tu fecha de nacimiento?",      ## CALENDARIO
                                      datetime.datetime.now(),
                                      datetime.date(1900, 1, 1),
                                      datetime.date(2030, 1, 1),
                                      format="DD/MM/YYYY",
                                      )
    fechaDeNacimiento = fechaDeNacimiento.strftime("%d/%m/%Y")        ### formato de fecha para la claseNumerologia
    actual = datetime.datetime.now().strftime("%d/%m/%Y")             ### fecha actual

continuar = (':violet[Si quieres continuar tu aprendizaje, en el menú tienes más '
             'opciones para enriquecer tu mundo interior]')    ### pie de página
st.header(':violet[El camino del Zenit]')   ### cabecera
st.markdown("***El Zenit es el punto  más alto situado sobre tu vertical.***")
st.write("")
st.write(":moon: **____El recorrido que puedes hacer en esta página te ayudará a conocer nuevos aspectos de "
         "tu personalidad.____** :moon:")


if nombre != "" and fechaDeNacimiento != actual:        ## solicitar datos principales

    fecha = Numerologia(fechaDeNacimiento)
    numeroP = fecha.numeroPersonal()
    principio = fecha.numero()
    nombreUsuario = NombreN(nombre)

    ## DESPLEGABLE CENTRAL CON OPCIONES
    opcion = ("Elige una opcion",
              "Número personal según tu fecha de nacimiento",
              "Vibración del nombre",
              "Tu signo del zodíaco",
              "Cartas de Tarot",
              "Tip's exclusivos para ti",
              "Terminar",)
    opcionElegida = opciones(opcion)         ## funcion: desplegable

    if opcionElegida == "Número personal según tu fecha de nacimiento":
        st.header(numeroP)

        if numeroP ==11:
            st.markdown(f"{nombre.title()} ***tienes un numero maestro***")
        elif numeroP > 11:
            st.markdown(f"{nombre.title()} ***tienes un fecha kármica***")


        ## MENU DE ESTA-OPCIÓN DENTRO DEL DESPLEGABLE CENTRAL
        tab1, tab2, tab3 = st.tabs([":violet[info]", ":violet[Lección de vida]", ":violet[Curiosidades de tu número personal]"])

        with tab1:
            st.write(" El número personal se calcula, sumando los dígitos de tu fecha de nacimiento")
            st.write("")
            st.markdown(f"Fecha ejemplo: 03/02/1990 ----> 0+3+0+2+1+9+9+0 = 6")
            st.markdown(f" ***Número personal 6***")
            st.write("")
            st.markdown(f"Fecha ejemplo: 03/02/2008 ----> 0+3+0+2+2+0+0+8 = 15  ----> 1+5 = 6")
            st.markdown(f" ***Fecha kármica 15 y número personal 6*** ")
            st.write("")
            st.markdown(f" :star: En el cálculo del :violet[número personal] se tienen en cuenta las "
                        f" ***fechas kármicas*** y siempre se reducen a un solo dígito, "
                        f"salvo el 11 que es ***número maestro***")


        with tab2:

            st.markdown(f":book: {principio[0]}")
            st.markdown(f":star: {principio[1]}")
            st.markdown(f":star: {principio[2]}")
            st.markdown(f":star: {principio[3]}")
            if numeroP in [13,15,16,19]:
                suma1 = int(numeroP // 10)
                suma2 = int(numeroP % 10)
                suma = suma1 + suma2
                archivo = f"archivos/numerosPersonales/{suma}"
                with open(archivo, encoding="utf-8") as datos:
                    contenido = datos.read()
                    contenido2 = contenido.split("@")
                datos.close()
                st.markdown(f":book: {contenido2[0]}")
                st.markdown(f":star: {contenido2[1]}")
                st.markdown(f":star: {contenido2[2]}")
                st.markdown(f":star: {contenido2[3]}")
                st.write("")
            st.caption(continuar)

        with tab3:
            historico = fecha.numeroHistorico()
            st.write(historico[0])
            st.markdown(f":star: {historico[1]}")
            st.markdown(f":star: {historico[2]}")
            st.markdown(f":star: {historico[3]}")


    elif opcionElegida == "Vibración del nombre":
        significado = nombreUsuario.valoresletras()

        vibracion = nombreUsuario.significadoVibracion(significado)
        st.markdown(f" **El nombre {nombre.title()} posee una vibración que dice:**")
        st.markdown(f":star: {vibracion}")
        st.write(" ¿Te gustaría saber más..?")
        st.write("*******")
        st.write(" Estamos en construcción, en breve habrá mas informacion sobre la vibración de tu nombre")
        st.caption(continuar)


    elif opcionElegida == "Tu signo del zodíaco":
        signoZodiaco = fecha.zodiaco()
        image = Image.open(f"imagenes/imagenesZodiaco/{signoZodiaco[0]}")
        st.image(image, width=200)
        st.markdown(f":star: {signoZodiaco[1]}")
        st.markdown(f":star: {signoZodiaco[2]}")
        st.markdown(f":star: {signoZodiaco[3]}")

        st.write(" ¿Te gustaría saber más..?")
        st.write("*******")
        st.write(" Estamos en construcción, en breve habrá mas informacion sobre tu signo del zodíaco")
        st.caption(continuar)

    elif opcionElegida == "Cartas de Tarot":

        ## MENU DE ESTA-OPCION DENTRO DEL DESPLEGABLE CENTRAL
        tab1, tab2 = st.tabs([":red[Tirada una Carta de Tarot]", ":red[Tirada de tres cartas Tarot]"])

        with (tab1):

            girar = st.checkbox('Girar la carta')       ## ACCION DE REVERSO Y ANVERSO
            col1, col2 = st.columns([1,2])             ## MENU DE ESTA-OPCION
            tirada = cartaTarot()
            leer = LecturaTarot(tirada[0])
            lectura = leer.interpretacion()


            with col1:

                if girar:                       ## GIRAR AL ANVERSO
                    if tirada[0] in tirada[1]:
                        image = Image.open(f"imagenes/cartasTarot/{tirada[0]}.png")
                        st.image(image, caption=lectura[0].title(), width=200)


                    else:
                        image = Image.open(f"imagenes/cartasTarot/arcanos/{tirada[0]}.jpg")
                        st.image(image,caption=lectura[0].title(), width=200)

                else:                       ## REVERSO
                    image = Image.open("imagenes/cartasTarot/reverso/reverso200.png")
                    st.image(image, width=200)


            with col2:
                if not girar:
                    st.write("Haz click en la casilla de GIRAR para descubrir tu carta")
                else:

                    st.write(lectura[1])
            st.caption(continuar)

        with tab2:
            mostrar = st.checkbox('Girar las tres cartas')   ## ACCION DE REVERSO Y ANVERSO
            st.write("Haz click en la casilla de GIRAR para descubrir tus cartas")
            col1, col2, col3 = st.columns([1,1,1])           ## MENU DE ESTA-OPCION
            tirada = cartaTarot()
            tiradatres = triada()

            if mostrar:             ## MOSTRAR EL ANVERSO
                with col1:

                    leer1 = LecturaTarot(tiradatres[0])
                    lectura1 = leer1.interpretacion()


                    if tiradatres[0] in tirada[1]:

                        image = Image.open(f"imagenes/cartasTarot/{tiradatres[0]}.png")
                        st.image(image,caption=lectura1[0].title(), width=200 )
                        st.markdown(f" ***Situación que  viene de tu pasado***")
                        st.write("*****")
                        st.write(lectura1[1])

                    else:
                        image = Image.open(f"imagenes/cartasTarot/arcanos/{tiradatres[0]}.jpg")
                        st.image(image,caption=lectura1[0].title(), width=200)
                        st.markdown(f" ***Situación que  viene de tu pasado***")
                        st.write("*****")
                        st.write(lectura1[1])


                with col2:
                    leer2 = LecturaTarot(tiradatres[1])
                    lectura2 = leer2.interpretacion()

                    if tiradatres[1] in tirada[1]:
                        image = Image.open(f"imagenes/cartasTarot/{tiradatres[1]}.png")
                        st.image(image,caption=lectura2[0].title(),width=200 )
                        st.markdown(f" ***Tu preocupación principal***")
                        st.write("*****")
                        st.write(lectura2[1])
                    else:
                        image = Image.open(f"imagenes/cartasTarot/arcanos/{tiradatres[1]}.jpg")
                        st.image(image,caption=lectura2[0].title(), width=200)
                        st.markdown(f" ***Tu preocupación principal***")
                        st.write("*****")
                        st.write(lectura2[1])

                with col3:
                    leer3 = LecturaTarot(tiradatres[2])
                    lectura3 = leer3.interpretacion()

                    if tiradatres[2] in tirada[1]:
                        image = Image.open(f"imagenes/cartasTarot/{tiradatres[2]}.png")
                        st.image(image,caption=lectura3[0].title(), width=200)
                        st.markdown(f" ***Influencia que va aumentando***")
                        st.write("*****")
                        st.write(lectura3[1])

                    else:
                        image = Image.open(f"imagenes/cartasTarot/arcanos/{tiradatres[2]}.jpg")
                        st.image(image,caption=lectura3[0].title(), width=200)
                        st.markdown(f" ***Influencia que va aumentando***")
                        st.write("*****")
                        st.write(lectura3[1])
                st.write("")
                st.caption(continuar)

            else:       ##  REVERSO
                with col1:
                    image = Image.open("imagenes/cartasTarot/reverso/reverso200.png")
                    st.image(image, width=200)
                with col2:
                    image = Image.open("imagenes/cartasTarot/reverso/reverso200.png")
                    st.image(image, width=200)
                with col3:
                    image = Image.open("imagenes/cartasTarot/reverso/reverso200.png")
                    st.image(image, width=200)

    elif opcionElegida == "Tip's exclusivos para ti":
        ## MENU DE ESTA-OPCION DENTRO DEL DESPLEGABLE CENTRAL

        tab1, tab2 ,tab3,tab4,tab5 = st.tabs(["Info",":red[Velas]", ":orange[Libros]", ":violet[Amuletos]",":green[Varios]"])

        with tab1:
            st.subheader(f"{nombre.title()}")
            st.markdown(':candle: ***Los colores de las velas influyen en el estado de ánimo.***')
            st.markdown(':book: ***Los libros ofrecen otra perspectiva de las situaciones.*** ')
            st.markdown(':star: ***Los amuletos son un apoyo en muchos momentos de la vida.***')
            st.markdown("******")
            st.caption(continuar)
        with tab2:

            col1, col2 = st.columns([1, 1])
            with col1:
                opcion = ("Vela amarilla",
                          "Vela azul",
                          "Vela blanca",
                          "Vela naranja",
                          "Vela negra",
                          "Vela roja",
                          "Vela verde",
                          )
                ### esta lista de articulos debe estar en el mismo orden que el archivo de donde
                ### lee la información de cada contenido ((ARCHIVO TIPS VELAS))
                ### Y tb el mismo orden de donde coge los enlaces ((ARCHIVO ENLACES ))
                mostrar = Articulos(opcion)
                elemento = opcion.index(mostrar.opcionElegida)
                image = Image.open(f"imagenes/imagenesVelas/{mostrar.velas()[1][elemento]}")
                st.image(image, width=200)
                st.write(f"{nombre.title()}, ¿te gusta este vela para ti? "
                         f" Pincha [aquí]({mostrar.velas()[2][elemento]})")
            with col2:
                st.subheader(mostrar.velas()[0][elemento])
                st.write(mostrar.significadoVela(mostrar.opcionElegida))
            st.caption(continuar)

        with tab3:
            col1, col2 = st.columns([1, 1])
            with col1:
                opcion = ("Tus zonas erroneas",
                          "Los cuatro acuerdos",
                           )
                ### esta lista de articulos debe estar en el mismo orden que el archivo de donde
                ### lee la información de cada contenido ((ARCHIVO TIPS LIBROS))
                ### Y tb el mismo orden de donde coge los enlaces ((ARCHIVO ENLACES ))
                mostrar = Articulos(opcion)
                elemento = opcion.index(mostrar.opcionElegida)
                image = Image.open(f"imagenes/imagenesLibros/{mostrar.libros()[1][elemento]}")
                st.image(image, width=200)
                st.write(f"{nombre.title()}, ¿te gusta este libro para ti? "
                         f" Pincha [aquí]({mostrar.libros()[2][elemento]})")
            with col2:
                st.subheader(mostrar.libros()[0][elemento])
                st.write(mostrar.significadoLibro(mostrar.opcionElegida))
            st.caption(continuar)

        with tab4:
            col1, col2 = st.columns([1, 1])
            with col1:
                opcion = ("Ala de Angel",
                          "Nudo de Bruja",
                          "Runa nórdica",
                          "Moneda de la suerte",
                          )
                ### esta lista de articulos debe estar en el mismo orden que el archivo de donde
                ### lee la información de cada contenido ((ARCHIVO TIPS AMULETOS))
                ### Y tb el mismo orden de donde coge los enlaces ((ARCHIVO ENLACES ))
                mostrar = Articulos(opcion)
                elemento = opcion.index(mostrar.opcionElegida)
                image = Image.open(f"imagenes/imagenesAmuletos/{mostrar.amuletos()[1][elemento]}")
                st.image(image, width=200)
                st.write(f"{nombre.title()}, ¿te gusta este amuleto para ti? "
                         f" Pincha [aquí]({mostrar.amuletos()[2][elemento]})")
            with col2:
                st.subheader(mostrar.amuletos()[0][elemento])
                st.write(mostrar.significadoAmuleto(mostrar.opcionElegida))


        with tab5:
            st.write(" Estamos en construcción, en breve habrá más información disponible.")

            st.caption(continuar)



    elif opcionElegida == "Terminar":
        st.write(f"{nombre.title()} gracias por utilizar esta página en el camino de tu Zenit.")
        st.write(':blue[Hasta la próxima]')

### INFORMACIÓN PARA EL USUARIO PARA QUE SEPA DE QUE VA LA PÁGINA Y SOLICITAR DATOS PARA
### ACTIVAR EL DESPLEGABLE

else:
    st.markdown(":star: *Descubrirás tu número personal y la vibración de tu nombre*")
    st.write(":star: *Puedes conocer aspectos sobre tu signo del zodiaco* ")
    st.write(":star: *Sección de tarot, donde puedes realizar tu lectura de cartas*")
    st.write(":star: *Sección velas, amuletos y libros recomendados*")
    st.write("***¿Quieres empezar?***")
    st.write('Por favor, escribe tu :blue[nombre y fecha de Nacimiento]')


