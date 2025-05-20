agenda = {}
while True:
    print("1. Ver todos los contactos guardados")
    print("2. Agregar un contacto nuevo (nombre + número)")
    print("3. Eliminar un contacto por su nombre")
    print("4. Salir del programa")
    opcion = int(input("Selecciona una opcion: "))
    if opcion == 1:
        print(agenda)
    elif opcion == 2:
        nombre_nuevo = input("Como se llama el nuevo contacto: ")
        numero_nuevo = int(input("Cual es su sumero de telefono: "))
        agenda[nombre_nuevo] = numero_nuevo
        print("Contacto agregado")
        pass
    elif opcion == 3:
        borrar_nombre = input("Que contacto quires eliminar: ")
        if borrar_nombre in agenda:
            del agenda[borrar_nombre]
            print("Contacto eliminado")
        else:
            print("Contacto no encontrado")
    elif opcion == 4:
        break