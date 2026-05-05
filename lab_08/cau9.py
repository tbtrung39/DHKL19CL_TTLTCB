def tinh_toan(a, b):
    tong = a + b
    hieu = a - b
    tich = a * b    
    print("Tong:", tong)
    print("Hieu:", hieu)
    print("Tich:", tich)
    if b != 0:
        thuong = a / b
        print("Thuong:", thuong)
    else:
        print("Khong the chia cho 0")
a = input("Nhap so a: ")
a = float(a)
b = input("Nhap so b: ")
b = float(b)
tinh_toan(a, b)
    
