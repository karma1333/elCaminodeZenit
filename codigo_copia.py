from io import open
from funciones.desplegable import opciones
from clases.numerologia import *
from clases.tarot import *
import datetime
import streamlit as st
from PIL import Image




st.subheader(':violet[Numerologia], :violet[Tarot], :violet[Amuletos] :violet[y mucho más]...')
st.write(" El recorrido que puedes hacer en esta página te va ayudar a conocer y descubrir nuevos aspectos de tu personalidad  ")
#st.write(" ")
st.write("Para empezar debes el conocer el numero que representa tu  fecha de Nacimiento")
st.write(" o el significado de tu nombre ")



continuar = ':violet[Continúa el recorrido, descubre todas las opciones del menú y enriquece tu mundo interior]'

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
st.write(fechaDeNacimiento)
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
