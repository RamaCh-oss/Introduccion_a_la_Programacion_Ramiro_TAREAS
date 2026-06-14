contador = 0
num_mayor = 0
num_menor = 0

while True:
    try:      
        numero = int(input("Ingresar un numero"))
    except ValueError:
        print("Solo se permiten numeros enteros positivos")
        continue
    
    if numero == -1:
        break
        
    if numero < 0:
        print("Solo se permiten numeros enteros positivos")
        continue
    
    if contador == 0:
        num_mayor = numero
        num_menor = numero
    else:
        if numero < num_menor:
            num_menor = numero 
            
        if numero > num_mayor:
            num_mayor = numero
    
    contador = contador + 1
    
if contador > 0:
        
    print("Cantidad de numeros ingresados: " , contador)
    print("Numero menor: " , num_menor)
    print("Nunero mayor: " , num_mayor)
        
    