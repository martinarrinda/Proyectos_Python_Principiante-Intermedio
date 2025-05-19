while True:
    euros = float(input("Introduce la cantidad en euros: "))
    convertir = (input("¿A qué moneda quieres convertir? (usd/gbp/jpy): "))
    if convertir == "usd":
        conversor_usd= (euros * 1.1)
        redondear_conversor_usd = round(conversor_usd,1)
        print(f" {euros} euros son {redondear_conversor_usd} dolares.")
    elif convertir == "gbp":
        conversor_gbp= euros * 0.85
        redondear_conversor_gbp = round(conversor_gbp)
        print(f" {euros} euros son {redondear_conversor_gbp} libras.")
    elif convertir == "jpy":
        conversor_jpy= euros * 155.5
        redondear_conversor_jpy = round(conversor_jpy)
        print(f" {euros} euros son {redondear_conversor_jpy} yenes.")
    seguir = input("¿Quieres hacer otra conversión? (s/n):")
    if seguir == "n":
        break

    
