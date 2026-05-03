""" Lectura de datos desde un csv (Página 35)
Importación y lectura a un archivo csv
"""

import csv
import os

ruta = os.path.join(os.path.dirname(__file__), "personas.csv")

with open(ruta, mode="r", newline="", encoding="utf-8") as archivo:
    lector = csv.reader(archivo)
    encabezado = next(lector)
    filas = list(lector)

print("Encabezado:", encabezado)
print("Filas:", filas)