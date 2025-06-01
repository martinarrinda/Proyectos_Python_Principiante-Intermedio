while True:
    edad = int(input("¿Cuántos años tienes? "))
    sexo = input("¿Eres hombre o mujer? ").lower()
    peso = float(input("¿Cuánto pesas en kg? "))
    altura = float(input("¿Cuál es tu altura en cm? "))

    print("Nivel de actividad física:")
    print("1: Sedentario (poco o ningún ejercicio)")
    print("2: Ligero (1-3 días/semana)") 
    print("3: Moderado (3-5 días/semana)")               
    print("4: Activo (6-7 días/semana)")                   
    print("5: Muy activo (doble sesión, trabajo físico)")                
    actividad_opcion = int(input("Elige una opción (1-5): "))

    print("Objetivo físico:")
    print("1: Perder peso")
    print("2: Mantener peso")
    print("3: Ganar peso")
    objetivo = int(input("Elige una opción (1-3): "))

    if sexo == "hombre":
        TMB = 10 * peso + 6.25 * altura - 5 * edad + 5
    else:
        TMB = 10 * peso + 6.25 * altura - 5 * edad - 161

    factores = {1: 1.2, 2: 1.375, 3: 1.55, 4: 1.725, 5: 1.9}
    TMB_actividad = TMB * factores[actividad_opcion]

    if objetivo == 1:
        total = TMB_actividad - 500
        print(f"Para perder peso: {round(total)} kcal/día")
    elif objetivo == 2:
        print(f"Para mantener peso: {round(TMB_actividad)} kcal/día")
    elif objetivo == 3:
        total = TMB_actividad + 500
        print(f"Para ganar peso: {round(total)} kcal/día")

    seguir = input("¿Calcular otra vez? (s/n): ")
    if seguir.lower() == "n":
        break
