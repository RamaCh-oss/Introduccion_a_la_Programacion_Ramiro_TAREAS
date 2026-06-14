limiteActual = int(input("Ingrese limite de tarjeta"))

tipoTarjeta = int(input("Ingrese tipo de tarjeta"))

if tipoTarjeta == 1:
    print("Nuevo limite: " , (limiteActual * 0.25) + limiteActual)

elif tipoTarjeta == 2:
    print("Nuevo limite: " , (limiteActual * 0.35) + limiteActual)

elif tipoTarjeta == 3:
    print("Nuevo limite: " , (limiteActual * 0.40) + limiteActual)

else:
    print("Nuevo limite: " , (limiteActual * 0.50) + limiteActual)

