import random
while True:
    dado_jugador = random.randint(0,6)
    print(f"Tu número: {dado_jugador}")
    dado_maquina = random.randint(0,6)
    print(f"Número de la máquina: {dado_maquina}")
    if dado_maquina < dado_jugador:
        print("¡Has ganado!")
    elif dado_maquina > dado_jugador:
        print("¡Ha ganado la maquina!")
    elif dado_maquina == dado_jugador:
        print("¡Empate!")
    volver_a_jugar = input("¿Quieres volver a jugar? (s/n):")
    if volver_a_jugar == "n":
        break