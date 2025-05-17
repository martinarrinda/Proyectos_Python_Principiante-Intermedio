import random
x = random.randint(0,100)
escoger_numero = -1
while escoger_numero !=x:
    escoger_numero = int(input("Escoje el numero secreto del 0-100: "))
    if escoger_numero ==x:
        print(f"Has acertado el numero, el numero secreto es {x}")
    else:
        print("Numero incorrecto")
