codigoProducto = [11, 22, 33, 44, 55]
nombreProducto = ["Pan", "Harina", "Fideos", "Huevos", "Aceite"]
cantidadStock = [20, 15, 10, 40, 8]

opcion = 0

while opcion < 4:
    print("MENU DE TIENDA")
    print("1- Mostrar inventario")
    print("2- Vender Producto")
    print("3- Reponer Stock")
    print("4- Salir")
    
    opcion = int(input("Seleccionar una opcion: "))
    
    match opcion:
        case 1:
            
            for i in range(5):
                print(f"Codigo: {codigoProducto[i]}")
                print(f"Nombre: {codigoProducto[i]}")
                print(f"Stock: {codigoProducto[i]}")