def nhap_so():
    n = input("Nhap so nguyen: ")
    n = int(n)
    return n
def hien_thi(n):
    return print("So vua nhap la: ", n)
def nhi_phan(n):
    if n == 0:
        return "0"
    kq = ""
    while n > 0:
        r = n % 2
        kq = str(r) + kq
        n = n // 2
    return kq
def bat_phan(n):
    if n == 0:
        return "0"
    kq = ""
    while n > 0:
        r = n % 8
        kq = str(r) + kq
        n = n // 8
    return kq
def thap_luc_phan(n):
    if n == 0:
        return "0"
    he16 = "0123456789ABCDEF"
    kq = ""
    while n > 0:
        r = n % 16
        kq = he16[r] + kq
        n = n // 16
    return kq