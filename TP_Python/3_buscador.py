numeros = [11, 22, 3, 5, 20, 4, 10, 23, 44, 98]

buscador = int(input("ingresar numero a buscar: "))

i = 0
existe = False

while i < 10 and not existe:
    if numeros[i] == buscador:
        existe = True
    else:
        i += 1

if existe:
    print(f"el numero se encontro en la posicion {i}.")
else:
    print("numero no encontrado.")