nums = [0] * 10

for i in range(10):
    nums[i] = int(input("ingresar un numero"))
    
for i in range(9, -1, -1):
    print(nums[i])