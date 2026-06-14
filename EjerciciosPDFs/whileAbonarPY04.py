

while True:
    precio_producto = float(input("Ingresar valor del producto, o ingrese 0 para terminar"))
    
    if precio_producto == 0:
        break

    else: 
        pago = float(input("Ingresar cantidad a abonar"))
        
        if pago > precio_producto:
            print("Pago realizado, Vuelto: " , pago - precio_producto)
            
        elif pago == precio_producto:
            print("Pago realizado")
            
        else: print("Dinero Insuficiente")
            

        

