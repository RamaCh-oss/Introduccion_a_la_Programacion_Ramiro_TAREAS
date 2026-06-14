salario = float(input("Ingresar salario mensual: "))
porcentaje_ahorro = float(input("Ingresar porcentaje de ahorro por mes: "))
precio_producto = float(input("Ingresar precio del producto: "))

ahorro_mensual = salario * (porcentaje_ahorro / 100)

if ahorro_mensual <= 0:
    print("No hay ahorro mensual")
    
else: 
    meses = precio_producto / ahorro_mensual

    import math
    meses_necesarios = math.ceil(meses)
    
    print("Meses hasta poder comprar el producto: " , meses_necesarios)