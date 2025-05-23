import random
abecedario = ["a","b","c","d","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
caracteres_especiales = ["!","@","$","%","&","/","(",")","+","^","*","-"]
while True:
    longintud = int(input("Cuanto queires que sea la lontitud de la contraseña: "))
    input_abecedario = int(input("Cuantas letras queires que tenga: "))
    input_caracteres = int(input("Cuantos caracteres especiales queires que tenga: "))
    input_numeros= int(input("Cuantos numeros queires que tenga: "))
    contraseña = []
    for i in range(input_abecedario):
            abercedario_random = random.choice(abecedario)
            contraseña.append(abercedario_random)
    for i in range(input_caracteres):
            caracteres_especiales_random = random.choice(caracteres_especiales)
            contraseña.append(caracteres_especiales_random)
    for i in range(input_numeros):
            numeros_random = str(random.randint(1,input_numeros))
            contraseña.append(numeros_random)
    random.shuffle(contraseña)
    resultado_final = "".join(contraseña)
    print(f"Tu contraseña es: {resultado_final} ")
    seguir_jugando = input("Quieres seguir jugando? s/n:")
    if seguir_jugando == "n":
           break
