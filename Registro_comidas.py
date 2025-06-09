import datetime
while True:
    print("1. Registrar una comida")
    print("2. Ver historial")
    print("3. Salir")
    opcion = int(input("Selecciona una opcion 1-3: "))
    if opcion == 1:
        comida = input("Que has comido: ")
        calorias = int(input("Cuantas kcal/100g: "))
        gramos = int(input("Cauntos gramos has comido?"))
        total = round (calorias * (gramos/100), 2)
        x = datetime.datetime.now().strftime("%H:%M,%d/%m/%Y")
        completo = (f"Fecha:{x}, Comida: {comida}, Calorias: {total}")
        with open ("comidas.csv","a") as archivo:
            archivo.write(completo + "\n")
    elif opcion == 2:
        print("Historial:")
        with open ("comidas.csv","r") as archivo:
            for linea in archivo:
                print(linea.strip())
    elif opcion == 3:
        break