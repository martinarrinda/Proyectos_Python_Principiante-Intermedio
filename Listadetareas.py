seleccion = []
while True:
    print("1. Ver la lista de tareas.")
    print("2. Agregar nuevas tareas.")
    print("3. Eliminar tareas por número.")
    print("4. Salir del programa.")
    opciones = int(input("Seleccione un numero: "))
    if opciones == 1:
        print(seleccion)
    elif opciones == 2:
        añadir = input("Que quieres añadir?")
        seleccion.append(añadir)
        print(seleccion)
    elif opciones == 3:
        quitar = ("Que numero quires quitar?")
        print(seleccion)
        borrar = seleccion.find(quitar)        
    elif opciones == 4:
        break   