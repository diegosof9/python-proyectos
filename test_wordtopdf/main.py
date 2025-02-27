# Importamos el paquete
import os
from docx2pdf import convert

# dropbox_ruta_relativa = 'Dropbox/test_wordtopdf'
directorio_actual = os.path.dirname(os.path.abspath(__file__))
# Convertimos directamente
# convert("test.docx")
# Podemos definir un archivo PDF de salida
# convert("test", "test.pdf")
# O también convertir todo el contenido de una carpeta
# convert("/Dropbox/test_wordtopdf")
# ruta_archivo_dropbox = os.path.join(directorio_actual, dropbox_ruta_relativa)

# print(directorio_actual)

convert(directorio_actual)

print("fin del proceso...")