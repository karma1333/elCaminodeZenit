from io import open
from funciones.desplegable import opciones
from clases.numerologia import *
from clases.tarot import *
from clases.nombre import *
import datetime
import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="El camino del Zenit",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)
##### codigos
# image = Image.open("imagenes/prueba.jpg")
    #
    # st.image(image, caption='numero')


with st.sidebar:    ## desplegable de la derecha

    st.write("Empezaremos por conocer el significado de tu número personal a través de la fecha de nacimiento,")
    nombre = st.text_input(" ¿Como te llamas?")
    fechaDeNacimiento = st.date_input("Cúal es tu fecha de nacimiento",      ###calendario
                                      datetime.datetime.now(),
                                      datetime.date(1900, 1, 1),
                                      datetime.date(2030, 1, 1),
                                      format="DD/MM/YYYY",
                                      )
    fechaDeNacimiento = fechaDeNacimiento.strftime("%d/%m/%Y")        ### formato de fecha para la claseNumerologia
    actual = datetime.datetime.now().strftime("%d/%m/%Y")             ### fecha actual

continuar = (':violet[Si quieres continuar el camino del Zenit, en el menú tienes más '
             'opciones para enriquecer tu mundo interior]')    ## pie de página
st.header(':violet[El camino del Zenit]')   ## cabecera
st.write(" El recorrido que puedes hacer en esta página te ayudará a conocer y descubrir nuevos aspectos de tu personalidad.  ")

if nombre != "" and fechaDeNacimiento != actual:         ### menú desplegable lateral

    fecha = Numerologia(fechaDeNacimiento)
    numeroP = fecha.numeroPersonal()
    principio = fecha.numero()
    nombreUsuario = NombreN(nombre)


    opcion = ("Elige una opcion",
              "Tu número personal según tu fecha de nacimiento",
              "Conocer la lección de Vida, según tu número personal",
              "La historia de tu número personal",
              "Significado de tu nombre",
              "Tu carta de tarot para hoy",
              "Tu signo del zodiaco",
              "Terminar",
              "Tarot")
    opcionElegida = opciones(opcion)

    if opcionElegida == "Tu número personal según tu fecha de nacimiento":
        st.markdown(f'***{nombre.title()} tu número personal es el {numeroP}***')
        st.header(numeroP)
        st.write(principio[0])
        st.caption(continuar)

    elif opcionElegida == "Conocer la lección de Vida, según tu número personal":
        st.write(principio[1])
        st.caption(continuar)

    elif opcionElegida == "La historia de tu número personal":
        historico = fecha.numeroHistorico()
        st.write(historico)
        st.caption(continuar)

    elif opcionElegida == "Tu signo del zodiaco":
        signoZodiaco = fecha.zodiaco()
        st.write(signoZodiaco)
        st.write(f" {nombre.title()} esta sección está en construcción ")
        st.caption(continuar)

    elif opcionElegida == "Significado de tu nombre":
        significado = nombreUsuario.valoresletras()
        st.header(significado)

    elif opcionElegida == "Terminar":
        st.write(" Gracias por participar en este proyecto")
        st.caption(continuar)

    elif opcionElegida == "Tarot":

        tab1, tab2 = st.tabs(["Tirada una Carta de Tarot", "Tirada de tres cartas Tarot"])

        with tab1:
            girar = st.checkbox('Girar la carta')
            col1, col2 = st.columns([1, 2])
            tirada = cartaTarot()

            with col1:

                if girar:
                    if tirada[0] in tirada[1]:
                        image = Image.open(f"imagenes/cartasTarot/{tirada[0]}.png")
                        st.image(image, width=200)
                    else:
                        image = Image.open(f"imagenes/cartasTarot/arcanos/{tirada[0]}.jpg")
                        st.image(image, width=200)
                else:
                    image = Image.open("imagenes/cartasTarot/reverso/reverso200.png")
                    st.image(image, width=200)

            with col2:
                st.subheader("aqui vendría el texto")

        with tab2:
            mostrar = st.checkbox('Girar las tres cartas')
            col1, col2, col3 = st.columns([1,1,1])
            tirada = cartaTarot()
            tiradatres = triada()

            if mostrar:
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
                        st.write(" Esta carta indica:")

                    else:
                        image = Image.open(f"imagenes/cartasTarot/arcanos/{tiradatres[1]}.jpg")
                        st.image(image, width=200)
                        st.write(" Esta carta indica:")

                with col3:
                    if tiradatres[2] in tirada[1]:
                        image = Image.open(f"imagenes/cartasTarot/{tiradatres[2]}.png")
                        st.image(image, width=200)
                        st.write(" ESte carta indica:")

                    else:
                        image = Image.open(f"imagenes/cartasTarot/arcanos/{tiradatres[2]}.jpg")
                        st.image(image, width=200)
                        st.write(" ESte carta indica:")

            else:
                with col1:
                    image = Image.open("imagenes/cartasTarot/reverso/reverso200.png")
                    st.image(image, width=200)
                with col2:
                    image = Image.open("imagenes/cartasTarot/reverso/reverso200.png")
                    st.image(image, width=200)
                with col3:
                    image = Image.open("imagenes/cartasTarot/reverso/reverso200.png")
                    st.image(image, width=200)

        # # with tab3:
        #     st.subheader("Frase de hoy")
        #     st.image("https://static.streamlit.io/examples/owl.jpg", width=200)


else:
    st.write('Por favor, escribe tu :blue[nombre y fecha de Nacimiento]')


