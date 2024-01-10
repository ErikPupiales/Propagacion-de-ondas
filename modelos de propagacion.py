import math

print("Hola, Bienvenido al programa para cálculo de los modelos de propagación")
print("Nombre: Erik Pupiales, CITEL 04, PROPAGACION DE ONDAS")

while True:
    print("\nMenu:")
    print("a. Calcular pérdida de trayectoria en espacio libre")
    print("b. Calcular modelo Hokumara-Hata")
    print("c. Calcular extensión PSC del modelo Hata para frecuencias > de 1500")
    print("q. Salir")

    opcion = input("Seleccione una opción (a, b, c, q): ").lower()

    if opcion == 'a':
        try:
            f = float(input("Ingrese la frecuencia (en Hz): "))
            n = float(input("Ingrese el valor n: "))
            d = float(input("Ingrese la distancia (en metros): "))

            # Fórmula para calcular la pérdida de trayectoria en espacio libre
            respuesta = 20 * math.log10(f) + 10 * n * math.log10(d) - 147.56

            print(f"\nPérdida de trayectoria en espacio libre: {respuesta:.2f} dB")
        except ValueError:
            print("Por favor, ingrese valores numéricos para la frecuencia, valor n y distancia.")

    elif opcion == 'b':
        print("a. Ciudad pequeña o mediana")
        print("b. Gran ciudad")
        print("c. SubUrbana")
        print("d. Areas abiertas o rurales")
        print("q. Volver al menú principal")

        ciudad_tipo = input("Seleccione una opción (a, b, c, d, q): ").lower()

        if ciudad_tipo == 'a':
            try:
                fc = float(input("Ingrese la frecuencia fc (en Hz): "))
                hr = float(input("Ingrese la altura de la antena de recepción (en metros): "))
                ht = float(input("Ingrese la altura de la antena de transmisión (en metros): "))
                d = float(input("Ingrese la distancia (en kilómetros): "))
                
                # Fórmula para el factor de corrección
                L = (1.1 * math.log10(fc) - 0.7) * hr - (1.56 * math.log10(fc) - 0.8)
                # Formula para el modelo Hokumara Hata
                H = 69.55 + 26.16 * math.log10(fc) - 13.82 * math.log10(ht) - L + (44.9 - 6.55 * math.log10(ht)) * math.log10(d) 

                print(f"\nEl factor de corrección A(hr) es: {L:.2f} dB")
                print(f"\nPérdida de trayectoria según modelo Hokumara-Hata (ciudad pequeña o mediana): {H:.2f} dB")
            except ValueError:
                print("Por favor, ingrese valores numéricos para la frecuencia, altura de antenas y distancia.")
        
        elif ciudad_tipo == 'b':
            print("a. Frecuencia <= 300 MHz")
            print("b. Frecuencia >= 300 MHz")
            print("q. Volver al menú principal")

            frecuencia_tipo = input("Seleccione una opción (a, b, q): ").lower()

            if frecuencia_tipo == 'a':
                try:
                    fc = float(input("Ingrese la frecuencia fc (en Hz): "))
                    hr = float(input("Ingrese la altura de la antena de recepción (en metros): "))
                    ht = float(input("Ingrese la altura de la antena de transmisión (en metros): "))
                    d = float(input("Ingrese la distancia (en kilómetros): "))

                    # Fórmula para el factor de corrección
                    L = 8.29 * (math.log10(1.54 * hr))**2 - 1.1
                    # Formula para el modelo Hokumara Hata
                    H = 69.55 + 26.16 * math.log10(fc) - 13.82 * math.log10(ht) - L + (44.9 - 6.55 * math.log10(ht)) * math.log10(d) 

                    print(f"\nEl factor de corrección A(hr) es: {L:.2f} dB")
                    print(f"\nPérdida de trayectoria según modelo Hokumara-Hata (Gran ciudad, Frecuencia <= 300 MHz): {H:.2f} dB")
                except ValueError:
                    print("Por favor, ingrese valores numéricos para la frecuencia, altura de antenas y distancia.")
            
            elif frecuencia_tipo == 'b':
                try:
                    fc = float(input("Ingrese la frecuencia fc (en Hz): "))
                    hr = float(input("Ingrese la altura de la antena de recepción (en metros): "))
                    ht = float(input("Ingrese la altura de la antena de transmisión (en metros): "))
                    d = float(input("Ingrese la distancia (en kilómetros): "))

                    # Fórmula para el factor de corrección
                    L = 3.2 * (math.log10(11.75 * hr))**2 - 4.97
                    # Formula para el modelo Hokumara Hata
                    H = 69.55 + 26.16 * math.log10(fc) - 13.82 * math.log10(ht) - L + (44.9 - 6.55 * math.log10(ht)) * math.log10(d) 

                    print(f"\nEl factor de corrección A(hr) es: {L:.2f} dB")
                    print(f"\nPérdida de trayectoria según modelo Hokumara-Hata (Gran ciudad, Frecuencia > 300 MHz): {H:.2f} dB")
                except ValueError:
                    print("Por favor, ingrese valores numéricos para la frecuencia, altura de antenas y distancia.")
        
        elif ciudad_tipo == 'c':
            try:
                fc = float(input("Ingrese la frecuencia fc (en Hz): "))
                hr = float(input("Ingrese la altura de la antena de recepción (en metros): "))
                ht = float(input("Ingrese la altura de la antena de transmisión (en metros): "))
                d = float(input("Ingrese la distancia (en kilómetros): "))
                
                # Fórmula para el factor de correccion
                L = (1.1 * math.log10(fc) - 0.7) * hr - (1.56 * math.log10(fc) - 0.8) - 2 * (math.log10(fc/28))**2 - 5.4
                # Formula para el modelo Hokumara Hata
                H = 69.55 + 26.16 * math.log10(fc) - 13.82 * math.log10(ht) - L + (44.9 - 6.55 * math.log10(ht)) * math.log10(d) 

                print(f"\nEl factor de corrección A(hr) es: {L:.2f} dB")
                print(f"\nPérdida de trayectoria según modelo Hokumara-Hata (SubUrbana): {H:.2f} dB")
            except ValueError:
                print("Por favor, ingrese valores numéricos para la frecuencia, altura de antenas y distancia.")


        elif ciudad_tipo == 'd':
            try:
                fc = float(input("Ingrese la frecuencia fc (en Hz): "))
                hr = float(input("Ingrese la altura de la antena de recepción (en metros): "))
                ht = float(input("Ingrese la altura de la antena de transmisión (en metros): "))
                d = float(input("Ingrese la distancia (en kilómetros): "))
                
                # Fórmula para el factor de correccion
                L = (1.1 * math.log10(fc) - 0.7) * hr - (1.56 * math.log10(fc) - 0.8) - 4.78 * (math.log10(fc))**2 - 18.733 * (math.log10(fc)) - 40.98
                # Formula para el modelo Hokumara Hata
                H = 69.55 + 26.16 * math.log10(fc) - 13.82 * math.log10(ht) - L + (44.9 - 6.55 * math.log10(ht)) * math.log10(d) 

                print(f"\nEl factor de corrección A(hr) es: {L:.2f} dB")
                print(f"\nPérdida de trayectoria según modelo Hokumara-Hata (Áreas abiertas o rurales): {H:.2f} dB")
            except ValueError:
                print("Por favor, ingrese valores numéricos para la frecuencia, altura de antenas y distancia.")


        elif ciudad_tipo == 'q':
            continue

        else:
            print("Opción no válida. Por favor, seleccione 'a', 'b', 'c', 'd' o 'q'.")

    elif opcion == 'c':
        # Agrega aquí la lógica para calcular la extensión PSC del modelo Hata
        try:
                fc = float(input("Ingrese la frecuencia fc (en MHz): "))
                hr = float(input("Ingrese la altura de la antena de recepción (en metros): "))
                ht = float(input("Ingrese la altura de la antena de transmisión (en metros): "))
                d = float(input("Ingrese la distancia (en kilómetros): "))
                cm= float(input("ingrese el valor de CM:"))
                # Fórmula para el factor de corrección
                L = 3.2 * (math.log10(11.75 * hr))**2 - 4.97
                # Formula para el modelo PSC
                H = 46.3 + 33.9 * math.log10(fc) - 13.82 * math.log10(ht) - L + (44.9 - 6.55 * math.log10(ht)) * math.log10(d) + cm

                print(f"\nEl factor de corrección A(hr) es: {L:.2f} dB")
                print(f"\nPérdida de trayectoria según modelo PSC de Hata es: {H:.2f} dB")
        except ValueError:
                print("Por favor, ingrese valores numéricos para la frecuencia, altura de antenas y distancia.") 

    
        pass

    elif opcion == 'q':
        print("¡Hasta luego!")
        break

    else:
        print("Opción no válida. Por favor, seleccione 'a', 'b', 'c' o 'q'.")
