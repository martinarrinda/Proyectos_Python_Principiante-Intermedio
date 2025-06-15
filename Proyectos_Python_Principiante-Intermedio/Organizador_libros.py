import statistics
while True:
    print("1. Registrar libros leídos")
    print("2. Ver historial completo")
    print("3. Ver estadísticas")
    print("4. Salir")
    opcion = int(input("Elige una opcion 1-4: "))
    if opcion == 1:
        titulo = input("Titulo del libro: ")
        autor = input("Autor: ")
        año = int (input("Año en que lo leíste: "))
        nota = int(input("Nota del 1 al 10 que le das: "))
        completo = (f"{titulo}, {autor}, {año}, {nota}")
        with open ("libros.csv","a") as archivo:
            archivo.write(completo + "\n")
    if opcion == 2:
        print("Historial completo")
        with open ("libros.csv","r") as archivo:
            for linea in archivo:
                palabras = linea.split(",")
                n = palabras[3].split("\n")
                libro_titulo = palabras[0]
                libro_autor =  palabras[1]
                libro_año = palabras[2]
                libro_nota = n[0]
                x = (f"Titulo:{libro_titulo}, Autor:{libro_autor}, Año:{libro_año}, Nota:{libro_nota}")
                print(x)
    if opcion ==3:
        total = 0
        lista =[]
        lista_libros = []
        años = int(input("Selecciona un año para saber cuantos libros leiste ese año: "))
        with open ("libros.csv","r") as archivo:
            for linea in archivo:
                buscar_años = linea.split(",")
                libros = buscar_años[0]
                lista_libros.append(libros)
                titulos = int(buscar_años[2])
                if titulos == años:
                    total += 1
                notas = int(buscar_años[3])
                lista.append(notas)
        media = statistics.mean(lista)
        libro_mayor_nota = max(lista)
        posiscion_libro_mayor_nota = lista.index(libro_mayor_nota)
        final_nota_alta = lista_libros[posiscion_libro_mayor_nota]
        print(f"El año {años} leiste un total de {total} libros.")
        print(f"La media de puntuaciones es {media}/10.")
        print(f"La puntuacion mas alta la tiene el libro {final_nota_alta} con una nota de {libro_mayor_nota}/10.")
    if opcion == 4:
        break

        
