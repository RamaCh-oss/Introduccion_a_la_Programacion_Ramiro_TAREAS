cantidad1 = int(input("ingrese cantidad numerica 1: "))
cantidad2 = int(input("ingrese cantidad numerica 2: "))
cantidad3 = int(input("ingrese cantidad numerica 3: "))

if cantidad1 > cantidad2 and cantidad1 > cantidad3:
    print("Mayor numero ingresado: 1")

elif cantidad2 > cantidad1 and cantidad2 > cantidad3:
    print("Mayor numero ingresado: 2")

elif cantidad3 > cantidad1 and cantidad3 > cantidad2: 
    print("Mayor numero ingresado: 3")

