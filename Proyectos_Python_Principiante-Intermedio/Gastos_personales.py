import datetime
while True:
    print("1. Registrar gasto")
    print("2. Ver historial completo")
    print("3. Analizar gastos")
    print("4. Salir")
    opcion = int(input("Selecciona una opcion 1-4: "))
    if opcion == 1:
        concepto = input("En que has gastado? ")
        cantidad = input("Cuantos euros has gastado en eso? ")
        x = datetime.datetime.now().strftime("%d/%m/%Y")
        completo = (f"{x}, {concepto}, {cantidad}")
        with open("gastos.csv","a") as archivo:
            archivo.write(completo + "\n")
    elif opcion ==2:
        print("Historial completo:")
        with open ("gastos.csv","r") as archivo:
            for linea in archivo:
              print(linea.strip())
    elif opcion ==3:
        gasto_total = 0
        lista_gasto = []
        lista_donde = []
        lista_cuando = []
        with open ("gastos.csv","r") as archivo:
            for linea in archivo:
                comas = linea.split(",")
                gasto = int(comas [2])
                lista_gasto.append(gasto)
                donde = comas[1]
                lista_donde.append(donde)
                cuando = comas[0]
                lista_cuando.append(cuando)
                gasto_total += gasto
        print(f"El gasto total es de {gasto_total} euros.")
        menos = min(lista_gasto)
        posicion_menos = lista_gasto.index(menos)
        final_donde_min = lista_donde[posicion_menos]
        final_cuando_min = lista_cuando[posicion_menos]
        mas = max(lista_gasto)
        posicion_mas = lista_gasto.index(mas)
        final_donde_mas = lista_donde[posicion_mas]
        final_cuando_mas = lista_cuando[posicion_mas]
        print(f"Tu gasto mas alto fue en la fecha: {final_cuando_mas}, lo gastaste en un {final_donde_mas} y fueron {mas} euros.")
        print(f"Tu gasto mas bajo fue en la fecha: {final_cuando_min}, lo gastaste en un {final_donde_min} y fueron {menos} euros.")
    elif opcion == 4:
        break