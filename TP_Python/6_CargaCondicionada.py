arreglo = [0] * 20
cantidad_ingresada = 0

print("Ingresa números positivos. Finaliza con un negativo o al llegar a 20.")

while cantidad_ingresada < 20:
    num = int(input(f"Ingresar el numero {cantidad_ingresada + 1}: "))
    
    if num < 0:
        print("Se detecto un numero negativo")
        break # Rompe el ciclo Mientras
        
    arreglo[cantidad_ingresada] = num
    cantidad_ingresada += 1

if cantidad_ingresada > 0:
    suma = 0
    for i in range(cantidad_ingresada):
        suma += arreglo[i]
        
    promedio = suma / cantidad_ingresada
    print(f"Se ingresaron {cantidad_ingresada} numeros")
    print(f"Promedio de los numeros ingresados: {promedio}")
else:
    print("No hay numeros para sacar un promedio")