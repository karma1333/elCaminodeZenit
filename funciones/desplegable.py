import streamlit as st




def opciones(opcion):
    """ Seleccionar una opción en un desplegabe"""
    opcionElegida = st.selectbox('Elige una opción', opcion)
    return opcionElegida





