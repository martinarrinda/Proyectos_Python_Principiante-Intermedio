while True:
    estudio = []
    lunes = int(input("Cuantas horas estudiaste el lunes: "))
    martes = int(input("Cuantas horas estudiaste el martes: "))
    miercoles = int(input("Cuantas horas estudiaste el miercoles: "))
    jueves= int(input("Cuantas horas estudiaste el jueves: "))
    viernes = int(input("Cuantas horas estudiaste el viernes: "))
    sabado = int(input("Cuantas horas estudiaste el sabado: "))
    domingo = int(input("Cuantas horas estudiaste el domingo: "))
    estudio.append(f"Lunes: {lunes} horas.")
    estudio.append(f"Martes: {martes} horas.")
    estudio.append(f"Miercoles: {miercoles} horas.")
    estudio.append(f"Jueves: {jueves} horas.")
    estudio.append(f"Viernes: {viernes} horas.")
    estudio.append(f"Sabado: {sabado} horas.")
    estudio.append(f"Domingo: {domingo} horas.")
    with open("estudio.txt","a") as archivo:
        for linea in estudio:
            archivo.write(linea + "\n")
    with open("estudio.txt","r") as archivo:
        for linea in archivo:
            print(linea.strip())
    contador = 0
    lista = []
    with open("estudio.txt","r") as archivo:
            for linea in archivo:
                linea.strip()
                partes = linea.split(":")
                parte_con_numero = partes [1]
                pedazos = parte_con_numero.split()
                numero = int(pedazos[0])  
                lista.append(numero)
                contador += numero 
    media = contador/7
    print(f"Tu media diaria de estudio son {media} horas.")  
    hora_productiva = max(lista)
    print(hora_productiva)
    if lista[0] == hora_productiva:
         print(f"El dia mas porductivo fue Lunes con {hora_productiva} horas.")
    elif lista[1] == hora_productiva:
         print(f"El dia mas porductivo fue Martes con {hora_productiva} horas.")
    elif lista[2] == hora_productiva:
         print(f"El dia mas porductivo fue Miercoles con {hora_productiva} horas.")
    elif lista[3] == hora_productiva:
         print(f"El dia mas porductivo fue Jueves con {hora_productiva} horas.")
    elif lista[4] == hora_productiva:
         print(f"El dia mas porductivo fue Viernes con {hora_productiva} horas.")
    elif lista[5] == hora_productiva:
         print(f"El dia mas porductivo fue Sabado con {hora_productiva} horas.")
    elif lista[6] == hora_productiva:
         print(f"El dia mas porductivo fue Domingo con {hora_productiva} horas.")
         
    seguir = input("Quires registrar otra semana mas? si/no: ")
    if seguir == "no":
        break