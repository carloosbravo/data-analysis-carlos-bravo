import json
from openpyxl import Workbook
from datetime import datetime

def leer_json(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        datos = json.load(archivo)
    return datos


def calcular_salario_con_incremento(salario_str, edad):
    salario = float(salario_str.strip('$').replace(',', ''))
    if edad < 30:
        salario *= 1.1  # Incremento del 10% para empleados menores de 30 años
    return salario


def crear_excel(datos, nombre_archivo_excel):
    wb = Workbook()
    ws = wb.active
    ws.append(["Nombre", "Edad", "Salario", "Género", "Proyecto", "Email"])

    for empleado in datos:
        if empleado['proyect'] == 'GRONK':
            continue  # Saltar empleados del proyecto 'GRONK'

        salario_euros = f"{calcular_salario_con_incremento(empleado['salary'], empleado['age']):,.2f} €"
        ws.append([empleado['name'], empleado['age'], salario_euros, empleado['gender'], empleado['proyect'],
                   empleado['email']])

    wb.save(nombre_archivo_excel)


archivo_json = 'employees.json'

# leer el archivo JSON
datos = leer_json(archivo_json)

# nombre del archivo Excel que se creará
fecha_actual = datetime.now().strftime("%m-%Y")
nombre_archivo_excel = f"pagos-empleados-{fecha_actual}.xlsx"

# crear el archivo Excel con los datos
crear_excel(datos, nombre_archivo_excel)

print(f"archivo excel '{nombre_archivo_excel}' creado exitosamente.")
