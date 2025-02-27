from openpyxl import load_workbook

documento_excel = load_workbook('observaciones_FINAL.xlsx')

# print(documento_excel.get_sheet_names())

hoja_excel = documento_excel['Hoja1']

contador = 0
valor_1, valor_2 = '', ''
valor_E, valor_F, valor_G = 1, 1, 1

celdas = hoja_excel['C1':'D93561']

# Recorremos el rango de columnas dado
for fila in celdas:
    for celda in fila:
        
        # Se limpia la celda solo en caso de que no contenga el valor de cadena 'sin registro'
        """ if celda.value != 'sin registro':
            celda.value = celda.value.replace("_x000D_","").replace("\n","").replace(" ","") """

        # Se asigna el valor de 1 a la variable contador, esto para llevar el control de las celdas analizadas  
        contador += 1 

        # Si contador es igual a 1 entra para analizar el valor_1, que es el valor de la primera celda de la fila 
        if contador == 1:

            # Si el valor de la celda es diferente a 'sin registro' entra a la condicional
            if celda.value != 'sin registro':
                valor_1 = celda.value
                hoja_excel[f"E{valor_E}"] = len(celda.value)

                # Ciclo for para verificación
                """   for i in celda.value:
                    print(i,end=',')

                print(len(celda.value)) 
                print() """
            else:
                valor_1 = 'checar'
                hoja_excel[f"E{valor_E}"] = 0
            valor_E += 1
        
        # Si contador es igual a 0 entra para analizar el valor_2, que es el valor de la segunda celda de la fila 
        else:

            # Si el valor de la celda es diferente a 'sin registro' entra a la condicional
            if celda.value != 'sin registro':
                valor_2 = celda.value
                hoja_excel[f"F{valor_F}"] = len(celda.value)

                """  for i in celda.value:
                    print(i,end=',')
                
                print(len(celda.value))
                print() """
            else:
                valor_2 = 'checar'
                hoja_excel[f"F{valor_F}"] = 0
            valor_F += 1
            contador = 0

        # Análisis de los dos valores
        if contador == 0:
            if valor_1 == 'checar' or valor_2 == 'checar':
                hoja_excel[f"G{valor_G}"] = "CHECAR"
            elif len(valor_1) == len(valor_2):
                hoja_excel[f"G{valor_G}"] = "CORRECTO"
            else:
                hoja_excel[f"G{valor_G}"] = "INCORRECTO"    
            valor_G += 1

documento_excel.save('análisis_observaciones_entregaFINAL_test_2.xlsx')

print("PROCESO FINALIZADO...")