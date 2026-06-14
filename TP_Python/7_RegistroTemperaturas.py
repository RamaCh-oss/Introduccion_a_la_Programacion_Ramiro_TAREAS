dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
temperaturas = [0] * 7

for i in range(7):
    temperaturas[i] = float(input(f"Ingrese la temperatura del {dias[i]}: "))

opcion = ""

while opcion != "D":
    print("A) Ver todas las temperaturas")
    print("B) Ver el promedio")
    print("C) Ver el día más caluroso")
    print("D) Salir")
    
    opcion = input("Elige una opción: ")

    match opcion:
        case "A":
            for i in range(7):
                print(f"{dias[i]}: {temperaturas[i]}°")
        case "B":
            suma = 0
            for temp in temperaturas:
                suma += temp
            print(f"El promedio semanal es: {suma / 7:.2f}°")
        case "C":
            max_temp = temperaturas[0]
            dia_caluroso = dias[0]
            for i in range(1, 7):
                if temperaturas[i] > max_temp:
                    max_temp = temperaturas[i]
                    dia_caluroso = dias[i]
            print(f"El día más caluroso fue el {dia_caluroso} con {max_temp}°.")
        case "D":
            print("Saliendo del registro de temperaturas...")
        case _:
            print("Opción inválida.")