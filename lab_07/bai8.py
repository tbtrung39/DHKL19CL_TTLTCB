A = set()
n = int(input("Nhập số lượng phần tử trong tập hợp A: "))
for _ in range(n):
    element = input("Nhập phần tử (có thể là số nguyên, số thực hoặc chuỗi): ")
    if element.isdigit():
        A.add(int(element))
    else:
        try:
            A.add(float(element))
        except ValueError:
            A.add(element)
print("Tập hợp A:", A)
print("Số phần tử trong tập hợp A:", len(A))