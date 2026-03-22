hang = input("Nhập số hàng: ")
hang = int(hang)    
cot = input("Nhập số cột: ")
cot = int(cot)
for i in range(hang):
    for j in range(cot):
        print("*", end=" ")
    print()