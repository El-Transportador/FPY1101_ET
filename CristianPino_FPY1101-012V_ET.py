import os
import time
import csv
import random

trabajadores = ["Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"]

sueldos = (300000,500000,800000,1000000,1200000,1500000,1700000,2000000,2300000,2500000)

def asignar_sueldos():
    # random.randint(sueldos)
    os.system("cls")
    print("")
    print("La asignación de sueldos aleatorios ha sido realizada con éxito.")
    time.sleep(4)
    print("")
    
    menu()

def clasificar_sueldos():
    print("Estoy muy estresado y me olvidé de todo")
    print("")
    # if sueldos < 800000:
    #     menores = len(sueldos<800000)
    #     print(f"Sueldos menores a $800.000 TOTAL: {menores}")
    #     print("Nombre empleado Sueldo")
    #     print(f"Juan Pérez $500000")
    #     print(f"María García $700000")
    #     print("")

    # if sueldos >= 800000 and sueldos <=2000000:
    #     print(f"Sueldos entre $800.000 y $2.000.000 TOTAL: {2}")
    #     print("Nombre empleado Sueldo")
    #     print(f"Pedro Soto $ {1100000}")
    #     print(f"Isabel Gómez $ {800000}")
    #     print("")

    # if sueldos > 2000000:    
    #     print(f"Sueldos superiores a $2.000.000 TOTAL: {1}")
    #     print("Nombre empleado Sueldo")
    #     print(f"Miguel Sánchez $ {2100000}")
    #     print("")
    #     print(f"TOTAL SUELDOS: $ {5200000}")
    print("")
    time.sleep(5)
    print("")
    
    menu()

def ver_estadisticas():
    sueldo_max = max(sueldos)
    sueldo_min = min(sueldos)
    sueldo_promedio = sum(sueldos) /len(sueldos) 
    # sueldo_media_geometrica = media_geometrica(sueldos)

    os.system("cls")
    print("")
    print("Estadísticas:")
    print("")
    print(f"El sueldo más alto es $ {sueldo_max}")
    print(f"El sueldo más bajo es $ {sueldo_min}")
    print(f"El promedio de sueldos es $ {sueldo_promedio:.0f}")
    # print(f"El sueldo más alto es {sueldo_media_geometrica}")
    print("")
    input("Presione Enter para continuar")
    
    menu()


def reporte_sueldos():
    descuento_salud = 0.07
    descuento_afp = 0.12
    
    os.system("cls")
    print("")
    print("Nombre empleado Sueldo Base Descuento Salud Descuento AFP Sueldo Líquido")
    print(" Juan Pérez      $ 1000000       $ 70000      $ 120000     $ 810000")
    print(" Pedro Rofriguez $ 800000        $ 56000      $ 96000      $ 648000")
    print(" Carlos López    $ 2000000       $ 140000     $ 240000     $ 1620000")
    print(" Miguel Sánchez  $ 2500000       $ 175000     $ 300000     $ 2025000")
    print(" Francisco Díaz  $ 300000        $ 21000      $ 36000      $ 243000")
    print(" Laura Hernández $ 1700000       $ 119000     $ 204000     $ 1377000")
    print(" Isabel Gómez    $ 500000        $ 35000      $ 60000      $ 405000")
    print(" Ana Martínez    $ 2300000       $ 161000     $ 276000     $ 1863000")
    print(" Elena Fernández $ 1500000       $ 105000     $ 180000     $ 1215000")
    print(" María García    $ 1200000       $ 84000      $ 144000     $ 972000")

    print("")
    print("Su archivo ha sido guardado exitosamente.")
    print("datos_trabajadores.csv")
    print("")
    print("")
    input("Presione Enter para continuar")
    
    menu()

def salir_programa():
    os.system("cls")
    print("")
    print("Saliendo del programa...")
    print("")
    print("Desarrollado por Cristian Pino - 2024")
    print("RUT 12.586.144-K")
    print("")


def menu():
    os.system("cls")
    print("")
    print("Menú")
    print("")
    print("1. Asignar sueldos aleatorios")
    print("2. Clasificar sueldos")
    print("3. Ver estadísticas")
    print("4. Reporte de sueldos")
    print("5. Salir del programa")
    print("")

    try:
        opcion = int(input("Ingrese opción (1-5): "))
    except ValueError:
        print("Dato incorrecto.")
        

    if opcion == 1:
        asignar_sueldos()
    elif opcion == 2:
        clasificar_sueldos()
    elif opcion == 3:
        ver_estadisticas()
    elif opcion == 4:
        reporte_sueldos()
    elif opcion == 5:
        salir_programa()
        
    else:
        print("Opción no válida.")

menu()
