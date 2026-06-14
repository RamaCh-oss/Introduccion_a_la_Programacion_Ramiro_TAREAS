valorProducto = float(input("ingrese valor del producto a comprar"))

descuento = valorProducto * 0.20

impuesto = valorProducto * 0.21

precioFinal = (valorProducto - descuento) + impuesto

print("Precio con descuento: " , valorProducto - descuento)
print("Precio Final (con IVA): " , precioFinal)

