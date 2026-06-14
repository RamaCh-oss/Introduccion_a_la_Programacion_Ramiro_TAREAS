productos = ["Papas", "Gaseosa", "Galletas", "Caramelos", "Agua"]
precios = [300, 200, 400, 500, 100]

print("1. Papas")
print("2. Gaseosa")
print("3. Galletas")
print("4. Caramelos")
print("5. Agua")

eleccion = int(input("Ingresar numero del producto a comprar(1 al 5): "))

match eleccion:
    case 1 | 2 | 3 | 4 | 5:
        indice = eleccion - 1 
        print(f"Has elegido: {productos[indice]}")
        print(f"Debes pagar: ${precios[indice]}")
    case _:
        print("producto no existente.")