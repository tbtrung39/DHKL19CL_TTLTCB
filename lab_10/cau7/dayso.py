import random
def sinh_day_so(n):
    ds = []
    for i in range(n):
        x = random.randint(1, 100)
        ds.append(x)
    return ds
def hien_thi(ds):
    print("Day so:", ds)
def la_snt(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def snt_chia_het_7(ds):
    print("Cac so nguyen to chia het cho 7:")
    for x in ds:
        if la_snt(x) and x % 7 == 0:
            print(x)
def tong_so_le(ds):
    tong = 0
    for x in ds:
        if x % 2 != 0:
            tong = tong + x
    return tong
def la_scp(n):
    for i in range(n + 1):
        if i * i == n:
            return True
    return False
def liet_ke_scp(ds):
    co = False
    print("Cac so chinh phuong:")
    for x in ds:
        if la_scp(x):
            print(x, end=" ")
            co = True
    if co == False:
        print("Khong co so chinh phuong nao.")