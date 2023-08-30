from io import open
from funciones.desplegable import opciones
from clases.numerologia import *
from clases.tarot import *
from clases.nombre import *
import datetime
import streamlit as st
from PIL import Image
from codigoAmuletos import *

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
##### ENLACES ####



## DESPLEGABLE DE LA DERECHA
with st.sidebar:

    st.write("Empezaremos por conocer el significado de tu número personal a través de la fecha de nacimiento,")
    nombre = st.text_input(" ¿Como te llamas?")
    fechaDeNacimiento = st.date_input("Cúal es tu fecha de nacimiento",      ## CALENDARIO
                                      datetime.datetime.now(),
                                      datetime.date(1900, 1, 1),
                                      datetime.date(2030, 1, 1),
                                      format="DD/MM/YYYY",
                                      )
    fechaDeNacimiento = fechaDeNacimiento.strftime("%d/%m/%Y")        ### formato de fecha para la claseNumerologia
    actual = datetime.datetime.now().strftime("%d/%m/%Y")             ### fecha actual

continuar = (':violet[Si quieres continuar el camino del Zenit, en el menú tienes más '
             'opciones para enriquecer tu mundo interior]')    ### pie de página
st.header(':violet[El camino del Zenit]')   ### cabecera
st.write(" El recorrido que puedes hacer en esta página te ayudará a conocer y descubrir nuevos aspectos de tu personalidad.  ")

if nombre != "" and fechaDeNacimiento != actual:        ## solicitar datos principales

    fecha = Numerologia(fechaDeNacimiento)
    numeroP = fecha.numeroPersonal()
    principio = fecha.numero()
    nombreUsuario = NombreN(nombre)

    ## DESPLEGABLE CENTRAL CON OPCIONES
    opcion = ("Elige una opcion",
              "Número personal según tu fecha de nacimiento",
              "Vibración del nombre",
              "Tu signo del zodiaco",
              "Tirada de cartas de Tarot",
              "Tip's exclusivos para ti",
              "Terminar",)
    opcionElegida = opciones(opcion)         ## funcion: desplegable

    if opcionElegida == "Número personal según tu fecha de nacimiento":
        st.markdown(f'***{nombre.title()} este es tu número personal según tu fecha de Nacimiento***')
        st.header(numeroP)
        ## MENU DE ESTA-OPCIÓN DENTRO DEL DESPLEGABLE CENTRAL
        tab1, tab2 = st.tabs([":red[Lección de vida]", ":red[Historia de tu número personal]"])
        with tab1:
            st.write(principio[0])
            st.caption(continuar)
        with tab2:
            historico = fecha.numeroHistorico()
            st.write(historico)

    elif opcionElegida == "Vibración del nombre":
        significado = nombreUsuario.valoresletras()
        st.header(significado)

    elif opcionElegida == "Tu signo del zodiaco":
        signoZodiaco = fecha.zodiaco()
        st.write(signoZodiaco)
        st.write(f" {nombre.title()} esta sección está en construcción ")
        st.caption(continuar)

    elif opcionElegida == "Tirada de cartas de Tarot":
        ## MENU DE ESTA-OPCION DENTRO DEL DESPLEGABLE CENTRAL
        tab1, tab2 = st.tabs([":red[Tirada una Carta de Tarot]", ":red[Tirada de tres cartas Tarot]"])

        with tab1:
            girar = st.checkbox('Girar la carta')       ## ACCION DE REVERSO Y ANVERSO
            col1, col2 = st.columns([1, 2])             ## MENU DE ESTA-OPCION
            tirada = cartaTarot()

            with col1:

                if girar:                       ## GIRAR AL ANVERSO
                    if tirada[0] in tirada[1]:
                        image = Image.open(f"imagenes/cartasTarot/{tirada[0]}.png")
                        st.image(image, width=200)
                    else:
                        image = Image.open(f"imagenes/cartasTarot/arcanos/{tirada[0]}.jpg")
                        st.image(image, width=200)
                else:                       ## REVERSO
                    image = Image.open("imagenes/cartasTarot/reverso/reverso200.png")
                    st.image(image, width=200)

            with col2:
                st.subheader("aqui vendría el texto")

        with tab2:
            mostrar = st.checkbox('Girar las tres cartas')   ## ACCION DE REVERSO Y ANVERSO
            col1, col2, col3 = st.columns([1,1,1])           ## MENU DE ESTA-OPCION
            tirada = cartaTarot()
            tiradatres = triada()

            if mostrar:             ## MOSTRAR EL ANVERSO
                with col1:
                    if tiradatres[0] in tirada[1]:
                        image = Image.open(f"imagenes/cartasTarot/{tiradatres[0]}.png")
                        st.image(image, width=200 )
                        st.write(" ESte carta indica:")

                    else:
                        image = Image.open(f"imagenes/cartasTarot/arcanos/{tiradatres[0]}.jpg")
                        st.image(image, width=200)
                        st.write("esta carta indica")

                with col2:
                    if tiradatres[1] in tirada[1]:
                        image = Image.open(f"imagenes/cartasTarot/{tiradatres[1]}.png")
                        st.image(image,width=200 )
                        st.write(" ESte carta indica:")

                    else:
                        image = Image.open(f"imagenes/cartasTarot/arcanos/{tiradatres[1]}.jpg")
                        st.image(image, width=200)
                        st.write(" ESte carta indica:")

                with col3:
                    if tiradatres[2] in tirada[1]:
                        image = Image.open(f"imagenes/cartasTarot/{tiradatres[2]}.png")
                        st.image(image, width=200)
                        st.write(" ESte carta indica:")

                    else:
                        image = Image.open(f"imagenes/cartasTarot/arcanos/{tiradatres[2]}.jpg")
                        st.image(image, width=200)
                        st.write(" ESte carta indica:")

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
        st.write(f" {nombre.title()} esta sección está en construcción ")
        st.markdown(" ***seccion de velas, libros, amuletos y varios***")
        ## MENU DE ESTA-OPCION
        tab1, tab2 ,tab3,tab4,tab5 = st.tabs(["Info",":red[Velas]", ":orange[Libros]", ":violet[Amuletos]",":green[Varios]"])

        with tab1:
            st.write("Escoge la opción que quieres")
            st.write(" la selección es exclusiva para ti")


        with tab2:

            st.write('Los colores de las velas apropiadas para ti')
            st.markdown('Sigue este enlace ---> '
                        'https://www.amazon.es/Lumaland-Luma-Lab-Vela-Perfumada/dp/B08G1RDFWH?th=1')
            # image = Image.open("imagenes/cartasTarot/reverso/reverso200.png")
            # st.image(image, width=200)

        with tab3:

            st.write('Estos libros son los apropiados para ti')
            # image = Image.open("imagenes/cartasTarot/reverso/reverso200.png")
            # st.image(image, width=200)

        with tab4:

            st.write(' Estos amuletos son los apropiados para ti ')
            image = Image.open("archivos/imagenesAmuletos/alaAngel.png")
            st.image(image, width=200)
            st.write("Para comprar esto [aqui](https://www.amazon.es/)")


        with tab5:

            st.write('Estos son los varios apropiados para ti')
            ####
            opcion =  ("Elige una opcion",
                      "suerte",
                      "dinero",
                       "aaa",
                       "bbbbb",
                       "cccc")





            ####
            mostrar = Articulos(opcion)
            elemento = opcion.index(mostrar.opcionElegida) - 1
            st.write(f"{mostrar.amuletos()[0][elemento]}{mostrar.amuletos()[1][elemento]}{mostrar.amuletos()[2][elemento]}")
            amuleto1 = '(https://www.amazon.es/Hztyyier-Amuleto-cl%C3%A1sico-Suerte-Decoraci%C3%B3n/dp/B07VHZLRNC/ref=sr_1_10?keywords=amuletos+de+buena+suerte&qid=1693384521&sr=8-10)'
            st.write("pincha aqui [link]"+amuleto1)
            st.markdown('[https://www.amazon.es/]')
            ###
            st.write(
                "Para comprar pincha [aqui](https://www.amazon.es/)")
            ###
        st.caption(continuar)



    elif opcionElegida == "Terminar":
        st.write(f"{nombre.title()} gracias por utilizar esta página en tu camino del Zenit.")
        st.write(':blue[Hasta la próxima]')



else:                   ## SOLICITA INTRODUCIR DATOS PARA ACTIVAR EL DESPLAGABLE CENTRAL
    st.write('Por favor, escribe tu :blue[nombre y fecha de Nacimiento]')


