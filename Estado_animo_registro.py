import datetime
while True:
    estado = input("¿Cómo te sientes hoy? (elige entre: feliz, normal, triste): ")
    actividad = input("¿Qué actividad te hizo sentir mejor hoy? ")
    nota = input("¿Qué nota del 1 al 10 le das a tu día? ")
    x = datetime.datetime.now().strftime("%Y-%m-%d")
    completo = (f"Fecha: {x}, Estado: {estado}, Actividad: {actividad}, Nota:{nota}.")
    with open ("estado.txt","a") as archivo:
        archivo.write(completo)
    ver_actividad = input("Quires ver tu historial animico? Si/No ")
    if ver_actividad.strip().lower() == "si":
        with open("estado.txt","r") as archivo:
            for linea in archivo:
                print(linea.strip())
    elif ver_actividad.strip().lower() == "no":
        break
    
