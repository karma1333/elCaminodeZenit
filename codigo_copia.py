from io import open
from funciones.desplegable import opciones
from clases.numerologia import *
from clases.tarot import *
import datetime
import streamlit as st
from PIL import Image




st.subheader(':violet[El camino del Zenit]')
st.write(" El recorrido que puedes hacer en esta página te ayudará a conocer y descubrir nuevos aspectos de tu personalidad.  ")
#st.write(" ")
st.write("Empezaremos por conocer el significado de tu número personal a través de la fecha de nacimiento,")
st.write(" y después el significado de tu nombre.")



continuar = ':violet[Si quieres continuar el camino del Zenit, en el menú tienes más opciones para enriquecer tu mundo interior]'

#st.subheader('Escribe tu :blue[nombre y fecha de Nacimiento]')
#image = Image.open("imagenes/prueba.jpg")

#st.image(image, caption='numero')

nombre = st.text_input(" ¿Como te llamas?")
fechaDeNacimiento = st.date_input("Cúal es tu fecha de nacimiento",
                                  datetime.datetime.now(),
                                  datetime.date(1900, 1, 1),
                                  datetime.date(2030, 1, 1),
                                  format="DD/MM/YYYY",
                                  )
fechaDeNacimiento = fechaDeNacimiento.strftime("%d/%m/%Y")
actual = datetime.datetime.now().strftime("%d/%m/%Y")

if nombre != "" and fechaDeNacimiento != actual:

    fecha = Numerologia(fechaDeNacimiento)
    numeroP = fecha.numeroPersonal()
    principio = fecha.numero()

    opcion = ("Elige una opcion",
              "Tu número personal según tu fecha de nacimiento",
              "Conocer la lección de Vida, según tu número personal",
              "La historia de tu número personal",
              "Tu signo del zodiaco",
              "Tu carta de tarot para hoy",
              "Terminar")
    opcionElegida = opciones(opcion)

    if opcionElegida == "Tu número personal según tu fecha de nacimiento":
        st.markdown(f'***{nombre.title()} tu número personal es el {numeroP}***')
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

else:
    st.write(" Por favor introduce tu nombre y tu fecha de nacimiento")
