precioProducto = 4700

importe = int(input("Ingrese Cantidad a Abonar"))

if importe > precioProducto:
    print("Pago Realizado, Vuelto: " , importe - precioProducto)
    
elif importe == precioProducto:

    print("Pago realizado")

else: print("Dinero Insuficiente")
