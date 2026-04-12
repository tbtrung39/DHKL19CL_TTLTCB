#su dung lenh assert de xac minh rang tat ca cac so trong 1 list duoc nhap vao la chan
n = []
while True:
    x = input("Nhap so (nhap q de thoat): ")
    if x == 'q':
        break
    n.append(int(x))
assert all(x % 2 == 0 for x in n), "Tat ca cac so phai la chan"
print("Tat ca cac so trong list n la chan.")
