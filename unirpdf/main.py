import os
from datetime import datetime
from PyPDF2 import PdfMerger

fecha = datetime.now()
año = fecha.year
mes = fecha.month
dia = fecha.day

if mes < 10:
    mes = "0" + str(mes)

if dia < 10:
    dia = "0" + str(dia)

# print(mes)
# archivos_pdf = [
#     'HOJA 1.pdf', 
#     'HOJA 2.pdf',
#     'HOJA 3.pdf',
#     'HOJA 4.pdf',
#     'HOJA 5.pdf',
#     'HOJA 6.pdf',
#     'HOJA 7.pdf',
#     'HOJA 8.pdf',
#     'HOJA 9.pdf',
#     'HOJA 10.pdf'
#     ]

archivos_pdf = [f for f in os.listdir() if f.endswith('.pdf')]

print(archivos_pdf)

archivos_pdf.sort(key=len)

merger = PdfMerger()

for archivo in archivos_pdf:

    merger.append(archivo)

# nombre_archivo = input("Ingresa el nombre del archivo: ")

# merger.write(f'{nombre_archivo}.pdf')
# merger.close()
merger.write(f'{año}_{mes}_{dia} - Estadística Básica.pdf')
merger.close()

print("Se unieron los archivos \".pdf\". Proceso finalizado...")

os.startfile(f'{año}_{mes}_{dia} - Estadística Básica.pdf')