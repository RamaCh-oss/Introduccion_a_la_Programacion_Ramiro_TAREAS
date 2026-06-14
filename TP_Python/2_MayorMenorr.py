import random

arreglo = [0] * 15
for i in range(15):
    arreglo[i] = random.randint(1, 100) 

mayor = arreglo[0]
menor = arreglo[0]

for num in arreglo:
    if num > mayor:
        mayor = num
    if num < menor:
        menor = num

print(f"Arreglo: {arreglo}")
print(f"Mayor numero: {mayor}")
print(f"Menor numero: {menor}")