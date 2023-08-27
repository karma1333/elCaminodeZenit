import datetime
import streamlit as st

fechadeNacimiento = st.date_input("Cúal es tu fecha de nacimiento",datetime.datetime(2023,8,7))


st.write('Tu fecha de nacimiento es:',fechadeNacimiento)

""" if mas == "si":
          st.write(f" {nombre} tu número personal es el {numero}")
      else:
          break

      arroba = st.radio(f" {nombre.title()} ¿Quieres saber que más cuenta de ti tu número?", ("no", "si"))

      if arroba == "si":
         st.write(principio[1])

      else:
         break

      curiosidad = st.radio(f" {nombre} tu número personal tiene tb un significado mas profundo "
                                f"e histórico, ¿quieres saber a que me refiero?", ('no', "si"))
      if curiosidad == "si":
          historico = fecha.numeroHistorico()
          st.write(historico)
      else:
         break"""
