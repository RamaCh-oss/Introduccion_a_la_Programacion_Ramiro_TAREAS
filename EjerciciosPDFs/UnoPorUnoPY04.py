
articulos = 0
total = 0

while True: 
    precio = float(input("Ingresar precio del producto(terminar con 0)"))
    
    if precio == 0:
        break
    
    total += precio 
    articulos += 1
    
print ("Total de la compra: " , total)
print ("Cantidad de productos: " , articulos)


