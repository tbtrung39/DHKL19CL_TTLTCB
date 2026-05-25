def nhap_ma_tran(n):
    a = []
    for i in range(n):
        dong = []
        for j in range(n):
            x = input(f"a[{i}][{j}] = ")
            x = int(x)
            dong.append(x)
        a.append(dong)
    return a
def xuat_ma_tran(a):
    for dong in a:
        for x in dong:
            print(x, end=" ")
        print()
def chuyen_vi(a):
    n = len(a)
    b = []
    for i in range(n):
        dong = []
        for j in range(n):
            dong.append(a[j][i])
        b.append(dong)
    return b
def doi_xung(a):
    n = len(a)
    for i in range(n):
        for j in range(n):
            if a[i][j] != a[j][i]:
                return False
    return True