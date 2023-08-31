from clases.numerologia import *
from clases.tarot import *
from clases.nombre import *
import datetime
import streamlit as st
from PIL import Image
from clases.articulos import *

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
st.subheader('El Zenit es el punto  más alto situado sobre tu vertical.')
st.write(" El recorrido que puedes hacer en esta página te ayudará a conocer y descubrir nuevos aspectos de tu personalidad. ")
st.write("Elevarse sobre lo ya conocido y aprender cosas nuevas es El camino de tu Zenit")

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

        vibracion = nombreUsuario.significadoVibracion(significado)
        st.write(f" {nombre.title()} tu nombre tiene una vibración ")
        st.header(significado)
        st.write(vibracion)


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

        tab1, tab2 ,tab3,tab4,tab5 = st.tabs(["Info",":red[Velas]", ":orange[Libros]", ":violet[Amuletos]",":green[Varios]"])

        with tab1:
            st.subheader(f"{nombre.title()}")
            st.markdown("***Las velas, los libros y los amuletos son sugerencias apropiadas en El camino de tu Zenit***")
            st.caption(continuar)
        with tab2:
            st.write('Los colores de las velas influyen el estado de ánimo de las personas')
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
                st.image(image, caption=mostrar.velas()[0][elemento], width=200)
                st.write(f"{nombre.title()}, ¿te gusta este vela para ti? "
                         f" Pincha [aquí]({mostrar.velas()[2][elemento]})")
            with col2:
                st.header("Vela recomendada")
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
                st.image(image, caption=mostrar.libros()[0][elemento], width=200)
                st.write(f"{nombre.title()}, ¿te gusta este libro para ti? "
                         f" Pincha [aquí]({mostrar.libros()[2][elemento]})")
            with col2:
                st.header("Libro recomendado")
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
                st.image(image, caption=mostrar.amuletos()[0][elemento], width=200)
                st.write(f"{nombre.title()}, ¿te gusta este amuleto para ti? "
                         f" Pincha [aquí]({mostrar.amuletos()[2][elemento]})")
            with col2:
                st.header("Amuleto de la buena suerte")
                st.write(mostrar.significadoAmuleto(mostrar.opcionElegida))


        with tab5:
            st.write(" Estamos en construcción, en breve estará disponible toda la información")

            st.caption(continuar)



    elif opcionElegida == "Terminar":
        st.write(f"{nombre.title()} gracias por utilizar esta página en el camino de tu Zenit.")
        st.write(':blue[Hasta la próxima]')



else:                   ## SOLICITA INTRODUCIR DATOS PARA ACTIVAR EL DESPLAGABLE CENTRAL
    st.write("¿Quieres empezar?")
    st.write('Por favor, escribe tu :blue[nombre y fecha de Nacimiento]')


