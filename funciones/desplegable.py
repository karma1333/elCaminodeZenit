import streamlit as st




def opciones(opcion):
    """ Seleccionar una opción"""
    opcionElegida = st.selectbox('Elige una opción', opcion)
    return opcionElegida





