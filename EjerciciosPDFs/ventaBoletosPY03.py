precio_boleto = 1000

cantidad_boletos = int(input("Ingrese boletos a comprar"))

if cantidad_boletos > 5:
    print("No se puede realizar la venta")

else:
    print("Valor de los boletos: " , precio_boleto * cantidad_boletos)

