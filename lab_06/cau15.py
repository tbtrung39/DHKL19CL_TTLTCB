n = int(input("Nhập số người: "))
data = []
for i in range(n):
    name = input("Tên: ")
    age = int(input("Tuổi: "))
    score = float(input("Điểm: "))
    data.append((name, age, score))

data.sort(key=lambda x: (x[0], x[1], x[2]))
print("Sau khi sắp xếp:", data)