from io import open
from funciones.desplegable import opciones
from clases.numerologia import *
from clases.tarot import *
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

if nombre != "" and fechaDeNacimiento != actual:         ### menú desplegable central

    fecha = Numerologia(fechaDeNacimiento)
    numeroP = fecha.numeroPersonal()
    principio = fecha.numero()

    opcion = ("Elige una opcion",
              "Tu número personal según tu fecha de nacimiento",
              "Conocer la lección de Vida, según tu número personal",
              "La historia de tu número personal",
              "Tu signo del zodiaco",
              "Tu carta de tarot para hoy",
              "Terminar",
              "saber más")
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

    elif opcionElegida == "Tu carta de tarot para hoy":
        tirada = cartaTarot()
        st.write(f" {nombre.title()} tu carta es: {tirada[0]}")

    elif opcionElegida == "Terminar":
        st.write(" Gracias por participar en este proyecto")
        st.caption(continuar)

    elif opcionElegida == "saber más":
        st.write("Tipś de la suerte")

        tab1, tab2, tab3 = st.tabs(["Una Carta de Tarot", "Tirada de tres cartas", "Frase de hoy"])

        with tab1:
            st.subheader("Pulsa sobre la imagen para descubrir tu carta")
            image = Image.open("imagenes/cartasTarot/reverso.png")
            st.image(image, width=200)

        with tab2:
            col1, col2 = st.columns([1,2])
            with col1:
                st.header("A dog")
                st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
            with col2:
                st.write("es un perro")

        with tab3:
            st.header("An owl")
            st.image("https://static.streamlit.io/examples/owl.jpg", width=200)


else:
    st.write('Por favor, escribe tu :blue[nombre y fecha de Nacimiento]')


