n = input("Nhap so sinh vien: ")
n = int(n)
A = {}
i = 0
while i < n:
    ma = input("Nhap ma sinh vien (6 ky tu so): ")
    ten = input("Nhap ten sinh vien: ")
    diem = input("Nhap diem: ")
    diem = float(diem)
    diem = round(diem)
    A[ma] = {
        "ten": ten,
        "diem": diem
    }
    i = i + 1
print("Danh sach sinh vien theo diem giam dan:")
d = 10
while d >= 0:
    for ma in A:
        if A[ma]["diem"] == d:
            print("Ma: ", ma, ", Ten: ", A[ma]["ten"], ", Diem: ", A[ma]["diem"])
    d = d - 1