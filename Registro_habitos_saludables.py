while True:
    print("1. Registrar hábitos de hoy")
    print("2. Ver historial")
    print("3. Salir")
    opcion = int (input("Elige una opcion 1-3: "))
    if opcion == 1:
        registro = {}
        agua = int(input("¿Cuántos vasos de agua bebiste hoy? "))
        sueño = int(input("¿Cuántas horas dormiste? "))
        ejercicio = input("¿Hiciste ejercicio hoy? (Si/No) ")
        comida = input("¿Comiste saludable hoy? (Si/No)")
        registro["Agua:"] = agua
        registro["Sueño:"] = sueño
        registro["Ejercicio:"] = ejercicio
        registro["Comida:"] = comida
        linea = str(registro)
        with open("archivo.txt", "a") as archivo:
            archivo.write(linea+ "\n")
    elif opcion == 2:
        with open("archivo.txt","r") as archivo:
            for linea in archivo:
                print(linea.strip())
    elif opcion == 3:
        break