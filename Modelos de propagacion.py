import math

def calcular_perdida_trayectoria(frecuencia, distancia, n):
    perdida_trayectoria = 20 * math.log10(frecuencia) + 10 * n * math.log10(distancia) - 147.56
    return perdida_trayectoria

def calcular_a_hr(ciudad, frecuencia, altura_recepcion):
    if ciudad == 'a':
        return sub_menu_gran_ciudad(frecuencia, altura_recepcion)
    elif ciudad == 'b':
        return 1.1 * math.log10(frecuencia) - 0.7 * altura_recepcion - (1.56 * math.log10(frecuencia) - 0.8)
    elif ciudad == 'c':
        return 1.1 * math.log10(frecuencia) - 0.7 * altura_recepcion - (1.56 * math.log10(frecuencia) - 0.8) - 2 * (math.log10(frecuencia / 28))**2 - 5.4
    elif ciudad == 'd':
        return 1.1 * math.log10(frecuencia) - 0.7 * altura_recepcion - (1.56 * math.log10(frecuencia) - 0.8) - 4.78 * (math.log10(frecuencia))**2 - 18.733 * math.log10(frecuencia) - 40.98
    else:
        print("Opción de ciudad no válida.")
        return None

def sub_menu_gran_ciudad(frecuencia, altura_recepcion):
    print("\nSubmenú Gran Ciudad:")
    print("1. Frecuencia < 300 MHz")
    print("2. Frecuencia >= 300 MHz")

    opcion = input("Seleccione una opción (1 o 2): ")

    if opcion == '1':
        return 8.29 * (math.log10(1.54 * altura_recepcion))**2 - 1.1
    elif opcion == '2':
        return 3.2 * (math.log10(11.75 * altura_recepcion))**2 - 4.97
    else:
        print("Opción no válida para frecuencia en Gran Ciudad.")
        return None

def calcular_modelo_hokumara(fc, ht, a_hr, d):
    modelo_hokumara = 69.55 + 26.16 * math.log10(fc) - 13.82 * math.log10(ht) - a_hr + (44.9 - 6.55 * math.log10(ht)) * math.log10(d)
    return modelo_hokumara

def calcular_extension_psc(fc, hr):
    extension_psc = 3.2 * (math.log10(11.75 * hr))**2 - 4.97 * math.log10(fc) - 14.77 + 6.55 * math.log10(hr)
    return extension_psc

def menu():
    while True:
        print("Hola, Bienvenido al programa para calculo de los modelos de propagacion")
        print("Nombre:Erik Pupiales, CITEL 04, PROPAGACION DE ONDAS")
        print("\nMenu:")
        print("a. Calcular pérdida de trayectoria")
        print("b. Calcular modelo Hokumara-Hata")
        print("c. Calcular extensión PSC del modelo Hata")
        print("q. Salir")

        opcion = input("Seleccione una opción (a, b, c, q): ")

        if opcion == 'a':
            # Solicitar al usuario ingresar los valores de frecuencia, distancia y n
            frecuencia_str = input("Ingrese la frecuencia en Hz (en notación científica, por ejemplo, 1.9e9 para 1.9 GHz): ")
            distancia_str = input("Ingrese la distancia en metros: ")
            n_str = input("Ingrese el valor de n: ")

            # Convertir las cadenas a valores numéricos
            frecuencia = float(frecuencia_str)
            distancia = float(distancia_str)
            n = float(n_str)

            # Calcular la pérdida de trayectoria y mostrar el resultado
            perdida_trayectoria = calcular_perdida_trayectoria(frecuencia, distancia, n)
            print(f"La pérdida de trayectoria es: {perdida_trayectoria} dB")

        elif opcion == 'b':
            # Solicitar al usuario elegir el tipo de ciudad
            print("\nSeleccione el tipo de ciudad:")
            print("a. Gran Ciudad")
            print("b. Ciudad Pequeña o Mediana")
            print("c. Sub Urbana")
            print("d. Áreas Abiertas o Rurales")

            tipo_ciudad = input("Seleccione una opción (a, b, c, d): ")

            # Solicitar al usuario ingresar los valores para el modelo Hokumara-Hata
            frecuencia_str = input("Ingrese la frecuencia en Hz (en notación científica, por ejemplo, 1.9e9 para 1.9 GHz): ")
            altura_recepcion_str = input("Ingrese la altura de la antena de recepción en metros: ")

            # Convertir las cadenas a valores numéricos
            frecuencia = float(frecuencia_str)
            altura_recepcion = float(altura_recepcion_str)

            # Calcular el factor de corrección A(hr) según el tipo de ciudad
            a_hr = calcular_a_hr(tipo_ciudad, frecuencia, altura_recepcion)

            if a_hr is not None:
                # Solicitar al usuario ingresar la altura de la antena de transmisión
                altura_transmision_str = input("Ingrese la altura de la antena de transmisión en metros: ")
                
                # Convertir la cadena a valor numérico
                altura_transmision = float(altura_transmision_str)

                # Solicitar al usuario ingresar los valores para el modelo Hokumara-Hata
                distancia_str = input("Ingrese la distancia en metros: ")

                # Convertir las cadenas a valores numéricos
                distancia = float(distancia_str)

                # Calcular el modelo Hokumara-Hata y mostrar el resultado
                modelo_hokumara = calcular_modelo_hokumara(frecuencia, altura_transmision, a_hr, distancia)
                print(f"El modelo Hokumara-Hata es: {modelo_hokumara} dB")

        elif opcion == 'c':
            # Solicitar al usuario ingresar los valores para la extensión PSC del modelo Hata
            frecuencia_str = input("Ingrese la frecuencia en Hz (en notación científica, por ejemplo, 1.9e9 para 1.9 GHz): ")
            altura_recepcion_str = input("Ingrese la altura de la antena de recepción en metros: ")

            # Convertir las cadenas a valores numéricos
            frecuencia_psc = float(frecuencia_str)
            altura_recepcion_psc = float(altura_recepcion_str)

            # Calcular la extensión PSC y mostrar el resultado
            extension_psc_resultado = calcular_extension_psc(frecuencia_psc, altura_recepcion_psc)
            print(f"La extensión PSC del modelo Hata es: {extension_psc_resultado} dB")

        elif opcion == 'q':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elija una opción correcta.")

# Llamar a la función principal del menú
menu()
