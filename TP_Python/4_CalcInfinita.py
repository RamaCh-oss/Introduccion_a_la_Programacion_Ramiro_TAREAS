opcion = 0

while opcion < 5:
    
    print("1- Sumar")
    print("2- Restar")
    print("3- Multiplicar")
    print("4- Dividir")
    print("5- Salir")
    
    opcion = int(input("Seleccionar una opcion del 1 al 5: "))
    
    match opcion:
        case 1:
            num1 = int(input("ingresar 1er numero a sumar"))
            num2 = int(input("ingresar 2do numero a sumar"))

            suma = num1 + num2
            print(f"Resultado: {suma}")
        
        case 2:            
            num1 = int(input("ingresar 1er numero a restar"))
            num2 = int(input("ingresar 2do numero a restar"))
            
            resta = num1 - num2
            print(f"Resultado: {resta}")
        
        case 3:
            
            num1 = int(input("ingresar 1er numero a multiplicar"))
            num2 = int(input("ingresar 2do numero a multiplicar"))
            
            multiplicacion = num1 * num2
            print(f"Resultado: {multiplicacion}")
            
        case 4:
            num1 = int(input("ingresar 1er numero a dividir"))
            num2 = int(input("ingresar 2do numero a dividir"))
            
            division = num1 / num2
            print(f"Resultado: {division}")
            
        case 5:
            print("Programa terminado")
            
        
        
            

            