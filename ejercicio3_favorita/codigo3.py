"""
Este programa le pide al usuario que escriba una línea de su canción favorita
y luego la imprime alineada a la derecha de la terminal.
"""

# Tarea 1:
# Pedir al usuario que escriba su línea favorita de una canción
linea = input("Escribe una línea de tu canción favorita: ")

# Tarea 2:
# Alinear la línea a la derecha de la terminal
# Usamos .rjust(80) para mover el texto hacia la derecha
linea_alineada = linea.rjust(80)

# Tarea 3:
# Imprimir la línea alineada a la derecha
print(linea_alineada)
