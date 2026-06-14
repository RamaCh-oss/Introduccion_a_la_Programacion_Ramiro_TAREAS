cantidad_alumnos = int(input("Ingrese la cantidad de alumnos: "))

suma_notas = 0

for i in range(cantidad_alumnos):
    nota = float(input(f"Ingrese la nota del alumno {i+1}: "))
    suma_notas += nota

promedio = suma_notas / cantidad_alumnos

print(f"El promedio del curso es: {promedio}")
