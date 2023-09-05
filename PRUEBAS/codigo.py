from io import open
from funciones.desplegable import NumeroPersonal
from clases.numerologia import *




nombre = input(" ¿Como te llamas?")

fechaDeNacimiento = input( "Escribe tu fecha de Nacimiento en este formato DD/MM/AAAA, (ej. 12/02/1981)" )
fecha = Numerologia(fechaDeNacimiento)
numero = fecha.numeroPersonal()
principio = fecha.numero()




print(f" {nombre.title()}, esto es lo que tu fecha de Nacimiento dice de ti\n {principio[0]}")

mas = input("¿Quieres saber cúal es tu numero personal?")
while True:
    if mas == "Si" or "S" or "Yes" or "Y":
        print(f" {nombre} tu número personal es el {numero}")
        curiosidad = input(f" {nombre} tu número personal tiene tb un significado mas profundo "
                           f"e histórico, ¿quieres saber a que me refiero?")
        if curiosidad == "Si" or "S" or "Yes" or "Y":
           historico = fecha.numeroHistorico()
           print(historico)
        arroba = input("mas??")
        if arroba == "si":
            print(principio[1])

        break
    else:
        break










