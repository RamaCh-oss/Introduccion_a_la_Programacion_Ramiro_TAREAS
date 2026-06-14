nombres = [""] * 10
nota1 = [0.0] * 10
nota2 = [0.0] * 10
cantidad_alumnos = 0

opcion = 0

while opcion != 3:
    print("1. Registrar nuevo alumno y notas")
    print("2. Mostrar lista y promedios")
    print("3. Salir")
    
    opcion = int(input("Elegir una opción: "))
    
    match opcion:
        case 1:
            if cantidad_alumnos < 10:
                nombres[cantidad_alumnos] = input("Nombre del alumno: ")
                nota1[cantidad_alumnos] = float(input("Nota 1: "))
                nota2[cantidad_alumnos] = float(input("Nota 2: "))
                cantidad_alumnos += 1
                print("Aluno Registrado")
            else:
                print("Maxima capacidad de alumnos alcanzada.")
                
        case 2:
            if cantidad_alumnos == 0:
                print("No hay alumnos registrados.")
                
            else:
                for i in range(cantidad_alumnos):
                    promedio = (nota1[i] + nota2[i]) / 2
                    
                    print(f"Alumno: {nombres[i]}")
                    print(f"Nota 1: {nota1[i]}")
                    print(f"Nota 2: {nota2[i]}")
                    print(f"Promedio: {promedio:.2f}")
        case 3:
            print("Saliendo")
