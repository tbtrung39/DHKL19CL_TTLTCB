numbers = []
n = int(input("Bạn muốn nhập bao nhiêu số tự nhiên: "))

for i in range(n):
    num = int(input(f"Nhập số tự nhiên thứ {i+1}: "))
    numbers.append(num)
print("Danh sách Numbers:",numbers)
A = set(numbers)
print("Tập hợp A:", A)
