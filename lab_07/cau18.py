A = {}
n = input("Nhap so thi sinh ban dau: ")
n = int(n)
i = 0
while i < n:
    sbd = input("Nhap so bao danh: ")
    ten = input("Nhap ho va ten: ")
    diem = input("Nhap diem: ")
    diem = float(diem)
    A[sbd] = {
        "ten": ten,
        "diem": diem
    }
    i = i + 1
x = input("Nhap so bao danh can tra cuu: ")
if x in A:
    print("Ho va ten: ", A[x]["ten"])
    print("Diem: ", A[x]["diem"])
else:
    print("Khong tim thay. Nhap thong tin thi sinh moi:")
    ten = input("Nhap ho va ten: ")
    diem = input("Nhap diem: ")
    diem = float(diem)
    A[x] = {
        "ten": ten,
        "diem": diem
    }
    print("Da bo sung thi sinh moi.")
print("Danh sach thi sinh:")
print(A)