while True:
    print("1. Agregar nueva nota")
    print("2. Ver todas las notas")
    print("3. Salir")
    opcion = int(input("Selecciona una opcion: "))
    if opcion == 1:
        nueva_nota= input("Que quires escribir? ")
        with open("notas.txt","a") as archivo:
            archivo.write(f"{nueva_nota} \n")
    if opcion == 2:
        try:
            with open("notas.txt","r") as archivo:
                for linea in archivo:
                    print(linea.strip())
        except FileNotFoundError:
            print("Archivo no encontrado")
    if opcion == 3:
        break
