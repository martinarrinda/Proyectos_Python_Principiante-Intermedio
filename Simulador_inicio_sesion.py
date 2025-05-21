usuario_contraseña = {"Martin": "123456"}
intentos = 3
while True:
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")
    if usuario in usuario_contraseña and usuario_contraseña[usuario] == contraseña:
        print("Bienvenido Martin!")
    else:
        intentos -=1
        print(f"Contraseña o ususarios incorrectos. Te quedan {intentos} intentos.")
        if intentos == 0:
            break