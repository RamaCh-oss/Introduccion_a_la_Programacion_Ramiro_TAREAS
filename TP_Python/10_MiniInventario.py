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
                print(f"Nombre: {nombreProducto[i]}")
                print(f"Stock: {cantidadStock[i]}")
                
        case 2:
            
            codigo_vender = int(input("Ingresar codigo de producto: "))
            
            i = 0
            existe = False
            
            while i < 5 and not existe:
                if codigoProducto[i] == codigo_vender:
                    existe == True
                    
                    if cantidadStock[i] > 0:
                        cantidadStock[i] -= 1
                        print(f"Se vendio{nombreProducto[i]}, stock actual: {cantidadStock[i]} ")
                        
                    else: 
                        print("No hay stock para este producto")
                i += 1
        
        case 3:
            
            codigo_reponer = int(input("Ingresar codigo del producto: "))
            
            i = 0
            existe = False
            
            while i < 5 and not existe:
                
                if codigoProducto[i] == codigo_reponer:
                    existe == True
                    
                    cantidad_sumar = int(input("Ingresar cantidad a sumar al stock: "))
                    if cantidad_sumar > 0:
                        cantidadStock[i] += cantidad_sumar
                        print(f"Stock repuesto, stock actual: {cantidadStock[i]}")
                    else:
                        print("la cantidad debe ser mayor a 0.")
                i += 1
                
        case 4:
            print("Adios")
            
        case _:
            print("Opción no válida. Elegir un numero del 1 al 4")
            