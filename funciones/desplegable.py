import streamlit as st




def opciones(opcion):
    """ seleccionar una opción"""
    opcionElegida = st.selectbox('Elige una opción', opcion)
    return opcionElegida





