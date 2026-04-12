tu_so = int(input("Nhập tử số: "))
mau_so = 0

while mau_so == 0:
    mau_so = int(input("Nhập mẫu số (phải khác 0): "))
    if mau_so == 0:
        print("Mẫu số không thể bằng 0. Vui lòng nhập lại!")

print(f"Phân số vừa nhập là: {tu_so}/{mau_so}")