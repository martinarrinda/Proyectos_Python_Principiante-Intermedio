while True:
    peso = float(input("Cuanto pesas en kg: "))
    altura = float(input("Cuanto mides en metros: "))
    imc = peso/(altura*altura)
    imc_round = round(imc,2)
    print(f"Tu IMC es: {imc_round}")
    if imc_round < 18.5:
        print("Estas en el rango: Bajo peso.")
    elif imc_round >= 18.5 and imc_round <= 24.9:
        print("Estas en el rango: Normal.")
    elif imc_round >= 25 and imc_round <= 29.9:
        print("Estas en el rango: Sobrepeso.")
    elif imc_round >= 30 and imc_round <= 34.9:
        print("Estas en el rango: Obesidad grado I.")
    elif imc_round >= 35 and imc_round <= 39.9:
        print("Estas en el rango: Obesidad grado II.")
    elif imc_round >= 40:
        print("Estas en el rango: Obesidad grado III.")
    seguir = input("¿Calcular otro? (s/n): ")
    if seguir == "n":
        break
    