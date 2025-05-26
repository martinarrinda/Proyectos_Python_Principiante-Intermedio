import random
while True:
    maquina_numero = random.randint(0,100)
    max_intentos = 7
    usuario_intentos = 0
    while usuario_intentos < max_intentos:
        usuario_numero = int(input("Adivina el numero del 0-100: "))
        if usuario_numero == maquina_numero:
            usuario_intentos +=1
            print(f" Has acertado en {usuario_intentos} intentos!")
            break
        elif usuario_numero > maquina_numero:
            usuario_intentos +=1
            print("El numero es menor.")
        elif usuario_numero < maquina_numero:
            usuario_intentos +=1
            print("El numero es mayor.")
    if usuario_numero != maquina_numero:
        print(f"Has perdido. El número era {maquina_numero}")
    volver_a_jugar = input("Quieres volver a jugar? s/n:")
    if volver_a_jugar == "n":
        break