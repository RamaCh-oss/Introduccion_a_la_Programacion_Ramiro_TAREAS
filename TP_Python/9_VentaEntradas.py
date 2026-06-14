asientos = [0] * 10
opcion = 0

while opcion != 3:
    print("1. Ver asientos")
    print("2. Vender entrada")
    print("3. Salir")
    
    opcion = int(input("Seleccione una opción: "))
    
    match opcion:
        case 1:
            for i in range(10):
                estado = "Libre" if asientos[i] == 0 else "Ocupado"
                print(f"Asiento {i + 1}: {estado}")
                
        case 2:
            asiento_pedido = int(input("\nIngrese el número de asiento (1 a 10): "))
            
            #validacion de numero en el rango
            if 1 <= asiento_pedido <= 10:
                indice = asiento_pedido - 1 #convierto al indice
                
                if asientos[indice] == 0:
                    asientos[indice] = 1 #marco como ocupado
                    print("Asiento asignado correctamente")
                else:
                    print("Asiento ocupado, elegir otro")
            else:
                print("El asiento debe estar entre el 1 y el 10")
                
        case 3:
            print("Saliendo")
        case _:
            print("opvion no valida")