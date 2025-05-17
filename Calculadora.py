while True:
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    number = int(input("Elige una operación: "))
    if number == 1:
        suma1 = int(input("Ingresa el primer numero que quires sumar: "))
        suma2 = int(input("Ingresa el segundo numero que quires sumar: "))
        suma = suma1 + suma2
        print(f"La suma de {suma1} + {suma2} = {suma}")
    elif number == 2:
        resta1 = int(input("Ingresa el primer numero que quires restar: "))
        resta2 = int(input("Ingresa el segundo numero que quires restar: "))
        resta = resta1 - resta2
        print(f"La resta de {resta1} - {resta2} = {resta}")
    elif number == 3:
        multi1 = int(input("Ingresa el primer numero que quires multiplicar: "))
        multi2 = int(input("Ingresa el segundo numero que quires multiplicar: "))
        multi = multi1 * multi2
        print(f"La multiplicacion de {multi1} x {multi2} = {multi}")
    elif number == 4:
        division1 = int(input("Ingresa el primer numero que quires dividir: "))
        division2 = int(input("Ingresa el segundo numero que quires dividir: "))
        division = division1 / division2
        print(f"La division de {division1} / {division2} = {division}")
    elif number == 5:
        print("Adios")
        break
